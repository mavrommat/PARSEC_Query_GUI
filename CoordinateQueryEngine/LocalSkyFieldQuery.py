import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table
from matplotlib.path import Path  # Used for the 2D polygon math

class LocalSkyFieldQuery:
    def __init__(self, database_table, ra_col='ra', dec_col='dec'):
        self.database = database_table
        
        # Convert database into a single SkyCoord array
        #----- standard system is ICRS degrees --------
        self.catalog_coords = SkyCoord(
            ra=self.database[ra_col], 
            dec=self.database[dec_col], 
            unit=u.deg, 
            frame='icrs'
        )

    def _return_filtered_data(self, boolean_mask):
        """Helper method to return the rows of the database where the mask is True."""
        return self.database[boolean_mask]

    def query_circle(self, center_coord, radius):
        separations = self.catalog_coords.separation(center_coord)
        
        # True/False mask of objects inside the radius
        mask = separations <= radius
        
        return self._return_filtered_data(mask)

    def query_rectangle(self, center_coord, width, height):
        """Find objects within a box using a SkyOffsetFrame to prevent spherical distortion."""
        # Create a custom coordinate grid centered exactly on your target
        offset_frame = center_coord.skyoffset_frame()
        
        # Project all database coordinates onto this new grid
        offset_coords = self.catalog_coords.transform_to(offset_frame)
        
        # Wrap longitude so it goes from -180 to 180 instead of 0 to 360
        lon_offset = offset_coords.lon.wrap_at(180 * u.deg)
        lat_offset = offset_coords.lat
        
        # Check if objects fall within the +/- boundaries of the width and height
        mask_lon = np.abs(lon_offset) <= (width / 2)
        mask_lat = np.abs(lat_offset) <= (height / 2)
        
        # Both must be true
        mask = mask_lon & mask_lat
        return self._return_filtered_data(mask)

    def query_polygon(self, coords_list):
        """Find objects inside a polygon using flat-plane projection."""
        if len(coords_list) < 3:
            raise ValueError("A polygon requires at least 3 coordinates.")
        
        # Use the first vertex as the center of our projection plane
        center_coord = coords_list[0]
        offset_frame = center_coord.skyoffset_frame()
        
        # 1. Project the catalog onto the flat plane
        cat_offsets = self.catalog_coords.transform_to(offset_frame)
        cat_x = cat_offsets.lon.wrap_at(180 * u.deg).deg
        cat_y = cat_offsets.lat.deg
        points = np.column_stack((cat_x, cat_y))
        
        # 2. Project the polygon vertices onto the same flat plane
        vertices = []
        for vertex in coords_list:
            v_off = vertex.transform_to(offset_frame)
            vx = v_off.lon.wrap_at(180 * u.deg).deg
            vy = v_off.lat.deg
            vertices.append((vx, vy))
            
        # 3. Use Matplotlib's Path math to check which points are inside the shape
        poly_path = Path(vertices)
        mask = poly_path.contains_points(points)
        
        return self._return_filtered_data(mask)
