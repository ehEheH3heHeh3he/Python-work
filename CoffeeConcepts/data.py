import pandas as pd
import urllib.parse

def apple_to_google_maps_pin(apple_url):
    try:
        parsed = urllib.parse.urlparse(str(apple_url))
        query_params = urllib.parse.parse_qs(parsed.query)
        latlon = query_params.get('ll', [''])[0].replace(' ', '')
        if latlon:
            return f"https://www.google.com/maps?q={latlon}"
    except:
        pass
    return ''  # Return empty string if anything fails

# === Load Excel file with NO HEADER ===
input_file = 'Inthanin-convert to google map.xlsx'  # 🔁 Replace with your actual filename
df = pd.read_excel(input_file, header=None)

# === Convert Apple Maps URL in column D (index 3) ===
df[4] = df[3].apply(apple_to_google_maps_pin)  # Column E (index 4)

# === Save to new file, also with NO HEADER ===
output_file = 'converted_output.xlsx'
df.to_excel(output_file, index=False, header=False)

print(f"✅ Google Maps links written to: {output_file}")
