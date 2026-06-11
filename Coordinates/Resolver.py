import re
import pandas as pd
import astropy.units as u
from astropy.coordinates import SkyCoord, Galactic, BarycentricMeanEcliptic

class ObjectResolver:

    FRAME_ALIASES = {
        "icrs": "icrs",
        "eq": "icrs",
        "equatorial": "icrs",

        "gal": "galactic",
        "galactic": "galactic",

        "ecl": "ecliptic",
        "ecliptic": "ecliptic",
    }

    def __init__(self, df: pd.DataFrame):
        required = {"id", "ra", "dec"}
        missing = required - set(df.columns)

        if missing: raise ValueError(f"Missing required columns: {missing}")

        self.df = df

        # O(1) lookup 
        self.catalog_lookup = {}

        for idx, object_id in enumerate(df["id"]):
            normalized = self.normalize_identifier(str(object_id))

            if normalized:
                self.catalog_lookup[normalized] = idx

    @staticmethod
    def normalize_identifier(name: str) -> str:
    
        name = str(name).upper().strip()

        return re.sub(r"\s+", "", name)

    def _parse_coordinate_input(self, text: str) -> SkyCoord | None:
        text = text.strip()

        if not text: return None

        tokens = text.split(maxsplit=1)

        if len(tokens) > 1:
            prefix = tokens[0].lower()
            frame = self.FRAME_ALIASES.get(prefix)

            if frame:
                values = tokens[1]

                try: # Galactic
                    if frame == "galactic":
                        l_deg, b_deg = map(float, values.split())

                        return SkyCoord( l=l_deg * u.deg, b=b_deg * u.deg, frame=Galactic()).icrs


                    if frame == "ecliptic": # Ecliptic
                        lon_deg, lat_deg = map(float, values.split())

                        return SkyCoord(lon=lon_deg * u.deg, lat=lat_deg * u.deg, frame=BarycentricMeanEcliptic()).icrs


                    if frame == "icrs": # ICRS
                        values = tokens[1]

                        try:
                            return SkyCoord(values, unit=(u.hourangle, u.deg), frame="icrs")
                            
                        except Exception:
                            return SkyCoord(values, unit=(u.deg, u.deg),frame="icrs")

                except Exception:
                    return None

        return None

    @staticmethod
    def _build_coordinate_payload(coord: SkyCoord) -> dict:
        gal = coord.galactic
        ecl = coord.transform_to(BarycentricMeanEcliptic())

        return {
            "icrs_equatorial": {"ra_deg": float(coord.ra.deg),
                                "dec_deg": float(coord.dec.deg),

                "ra_hms": coord.ra.to_string(unit=u.hour, sep=":", precision=3),

                "dec_dms": coord.dec.to_string(sep=":", precision=2, alwayssign=True)
            },

            "galactic": {
                "l_deg": float(gal.l.deg),
                "b_deg": float(gal.b.deg)
            },

            "ecliptic": {
                "lon_deg": float(ecl.lon.deg),
                "lat_deg": float(ecl.lat.deg)
            }
        }

    def resolve(self, text: str) -> dict:
        payload = {
            "search_term": text,
            "status": "Not Found",
            "object_id": None,
            "icrs_equatorial": None,
            "galactic": None,
            "ecliptic": None
        }

        text = text.strip()

        if not text:
            return payload

        # Try coordinates first
        coord = self._parse_coordinate_input(text)

        # Try catalog identifier
        if coord is None:
            normalized = self.normalize_identifier(text)

            idx = self.catalog_lookup.get(normalized)

            if idx is None: return payload

            row = self.df.iloc[idx]

            coord = SkyCoord(ra=float(row["ra"]) * u.deg, dec=float(row["dec"]) * u.deg, frame="icrs")
            payload["object_id"] = row["id"]

        payload.update(self._build_coordinate_payload(coord))
        payload["status"] = "Resolved"

        return payload