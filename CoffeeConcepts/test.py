import pandas as pd

# Load the Excel file (no header)
df = pd.read_excel("final_cleaned_province_with_region.xlsx", header=None)

# Loop through rows and clear values that match
for index, row in df.iterrows():
    province = row[0]
    region = row[1]

    if (pd.isna(province) or str(province).strip().lower() == "nan") and region == "Northern":
        df.at[index, 0] = ""  # Clear province column
        df.at[index, 1] = ""  # Clear region column

# Save to a new Excel file
df.to_excel("cleaned_no_false_northern.xlsx", index=False, header=False)

print("✅ Saved to cleaned_no_false_northern.xlsx")
