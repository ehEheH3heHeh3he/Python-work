import pandas as pd
import urllib.parse

# Load your Excel file
input_file = "cafe_amazon_stores_with_region.xlsx"
df = pd.read_excel(input_file)

def create_google_maps_link(row):
    base_url = "https://www.google.com/maps/search/?api=1&query="
    # Combine store Name + Address for a more precise query
    combined = f"{row['Name']} {row['Address']}"
    query = urllib.parse.quote(str(combined))
    return base_url + query

# Apply function row-wise to combine name and address
df["Map"] = df.apply(create_google_maps_link, axis=1)

# Export to Excel
output_file = "cafe_amazon_stores_with_region_and_map.xlsx"
df.to_excel(output_file, index=False)

print(f"✅ Exported with combined Name+Address Google Maps URLs: {output_file}")
