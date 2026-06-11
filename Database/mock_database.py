import pandas as pd
from astroquery.simbad import Simbad

class AstroCatalogPipeline:
    def __init__(self):
        self.simbad = Simbad()

    def normalize_simbad_df(self, df):
        # Astroquery defaults to lowercase columns
        df.columns = [c.lower() for c in df.columns]

        required = ["main_id", "ra", "dec", "otype"]
        missing = [c for c in required if c not in df.columns]

        if missing:
            raise ValueError(f"Missing SIMBAD columns: {missing}")

        df = df[required].copy()

        # Decode byte strings 
        for col in ["main_id", "otype"]:
            if pd.api.types.is_object_dtype(df[col]):
                df[col] = df[col].apply(
                    lambda x: x.decode("utf-8") if isinstance(x, bytes) else x
                )

        return df

    # Fetch data using TAP / ADQL
    def fetch_galaxies(self):
        query = "SELECT TOP 15000 main_id, ra, dec, otype FROM basic WHERE otype = 'G'"
        result = self.simbad.query_tap(query)
        
        if result is None:
            return pd.DataFrame()
        
        df = result.to_pandas()
        return self.normalize_simbad_df(df)

    def build_full_catalog(self):
        df = self.fetch_galaxies()

        # Rename main_id to id
        df = df.rename(columns={"main_id": "id"})
        df = df.drop_duplicates(subset="id")
        
        return df

    
    def save(self, df, path="astro_catalog.parquet"):
        df.to_parquet(path, compression="zstd")


    def build_10k(self, df):
        # Sample exactly 10,000 rows
        df10k = df.sample(
            n=min(10000, len(df)),
            random_state=42
        ).reset_index(drop=True)

        return df10k

# Execution
if __name__ == "__main__":
    pipeline = AstroCatalogPipeline()

    print("Fetching data from SIMBAD via TAP...")
    df_full = pipeline.build_full_catalog()

    print("Building 10k subset...")
    df_10k = pipeline.build_10k(df_full)

    print(f"Saving 10k subset ({len(df_10k)} rows)...")
    pipeline.save(df_10k, "astro_10k.parquet")
    print("Done!")