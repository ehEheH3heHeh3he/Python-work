import json
import pandas as pd

# Load the data from the txt file
with open("ChaoDoiData.txt", "r", encoding="utf-8") as f:
    raw_data = f.read()

# Make sure the content is a valid list of dicts
if not raw_data.strip().startswith("["):
    raw_data = f"[{raw_data.strip().rstrip(',')}]"

data = json.loads(raw_data)

# Prepare rows for Excel
rows = []
for entry in data:
    title = entry.get("title", "")
    state = entry.get("state", "")
    lat = entry.get("lat", "")
    lng = entry.get("lng", "")
    # Generate Apple Maps link
    apple_maps_link = f"https://maps.apple.com/?ll={lat},{lng}&q={title}"
    rows.append(["Chao Doi", title, state, apple_maps_link])

# Create DataFrame
df = pd.DataFrame(rows, columns=["Chao Doi", "Title", "State", "Apple Maps Link"])

# Export to Excel
df.to_excel("chao_doi_locations.xlsx", index=False)
