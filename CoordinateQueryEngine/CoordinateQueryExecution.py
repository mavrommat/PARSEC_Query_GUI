import pandas as pd
import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord
from CoordinateQueryEngine.LocalSkyFieldQuery import LocalSkyFieldQuery
from Coordinates.Resolver import ObjectResolver 

class QueryExecutionEngine:
    def __init__(self, parquet_path="Database/astro_10k.parquet"):
        # Load database
        print(f"Loading database from {parquet_path}...")
        self.df = pd.read_parquet(parquet_path)
        
        # spatial query engine
        self.sky_query = LocalSkyFieldQuery(self.df, ra_col='ra', dec_col='dec')
        
        # resolver: string targets into coordinates
        self.resolver = ObjectResolver(df=self.df)

    def execute_payload(self, master_payload):
        
        all_areas = master_payload.get("Standard_Coordinates", []) + master_payload.get("Advanced_Coordinates", [])
        all_filtered_results = []

        for area in all_areas:
            shape = area.get("Shape")
            target_name = area.get("Target")
            
            # Map string units to Astropy units
            unit_str = area.get("Units", "Degrees")
            if unit_str == "Arcminutes":
                astropy_unit = u.arcmin
            elif unit_str == "Arcseconds":
                astropy_unit = u.arcsec
            else:
                astropy_unit = u.deg
            
            # Grab Distance if it exists 
            distance_raw = area.get("Distance", 0)
            distance_val = float(distance_raw) * astropy_unit if distance_raw else 0 * astropy_unit

            print(f"\nExecuting: {shape} for {target_name}...")

            # 1. Custom Polygon
            if shape == "Custom Polygon":
                coords_list = []
                for pt in area.get("coordinates", []):
                    if str(pt.get("active")) == "1": 
                        coords_list.append(SkyCoord(ra=pt['c1'], dec=pt['c2'], unit=u.deg))
                
                if len(coords_list) >= 3:
                    result_df = self.sky_query.query_polygon(coords_list)
                    all_filtered_results.append(result_df)

            # 2. Target-Based Shapes
            else:
                resolved = self.resolver.resolve(target_name)
                
                if resolved.get("status") == "Not Found":
                    print(f"Error: Could not resolve coordinates for {target_name}. Skipping area.")
                    continue
                
                ra = resolved["icrs_equatorial"]["ra_deg"]
                dec = resolved["icrs_equatorial"]["dec_deg"]
                center = SkyCoord(ra=ra, dec=dec, unit=u.deg)

                if shape == "Radius search":
                    result_df = self.sky_query.query_circle(center, distance_val)
                    all_filtered_results.append(result_df)

                elif shape == "Rectangle search":
                    # Extract Width and Height
                    width_val = float(area.get("Width", 0)) * astropy_unit
                    height_val = float(area.get("Height", 0)) * astropy_unit
                    
                    result_df = self.sky_query.query_rectangle(center, width=width_val, height=height_val)
                    all_filtered_results.append(result_df)

                elif shape == "Polygon search":
                    num_vertices = int(area.get("Vertices", 3))
                    vertices = self._generate_regular_polygon(center, distance_val, num_vertices)
                    result_df = self.sky_query.query_polygon(vertices)
                    all_filtered_results.append(result_df)

        return all_filtered_results

    def _generate_regular_polygon(self, center, radius, num_vertices):
        angles = np.linspace(0, 360, num_vertices, endpoint=False) * u.deg
        # directional_offset_by calculates exact spherical coordinates extending outward
        vertices = [center.directional_offset_by(angle, radius) for angle in angles]
        return vertices