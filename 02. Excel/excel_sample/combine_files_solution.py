import pandas as pd
import glob
import os

# Define folders and output file
input_folder = "products"
output_folder = "output"
output_file = "combined_products_with_commission.csv"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get all CSV files
csv_files = glob.glob(os.path.join(input_folder, "*.csv"))

# Read and combine CSV files
df_list = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(df_list, ignore_index=True)

# Remove completely empty rows
combined_df.dropna(how="all", inplace=True)

# Remove duplicate rows
combined_df.drop_duplicates(inplace=True)

# Clean Revenue column: remove $ and commas, convert to float
combined_df["Revenue"] = (
    combined_df["Revenue"]
    .replace(r"[\$,]", "", regex=True)
    .astype(float)
)

# Clean Commission Rate column: remove % and convert to decimal
combined_df["Commission Rate"] = (
    combined_df["Commission Rate"]
    .str.replace("%", "", regex=False)
    .astype(float) / 100
)

# Calculate Commission
combined_df["Commission"] = (
    combined_df["Revenue"] * combined_df["Commission Rate"]
).round(2)

# Save final combined file
output_path = os.path.join(output_folder, output_file)
combined_df.to_csv(output_path, index=False)

print(f"Combined file with commission saved to: {output_path}")
