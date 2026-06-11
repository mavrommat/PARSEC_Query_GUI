import pandas as pd

# Load the parquet file
df = pd.read_parquet("Database/astro_10k.parquet")

# Export it to a CSV file in the same folder
df.to_csv("Database/astro_10k_readable.csv", index=False)

print("astro_10k_readable.csv has been created")