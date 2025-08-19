from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

INPUT_FILE = "Punlinks.xlsx"
OUTPUT_FILE = "Punprovince.xlsx"

# Load data
df = pd.read_excel(INPUT_FILE, header=None)
df.columns = ['Google Maps URL']

# Setup Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Province extraction function with progress print
def extract_province(url, index):
    print(f"Row {index + 1}/{len(df)}: loading...")

    try:
        driver.get(url)
        time.sleep(4)

        elements = driver.find_elements(By.CSS_SELECTOR, 'span.DkEaL')
        for el in elements:
            text = el.text.strip()
            if text and "เพิ่มเว็บไซต์" not in text:
                words = text.split()
                province = words[-1].strip()
                print(f"Row {index + 1}: ✅ Found province: {province}")
                return province

        print(f"Row {index + 1}: ❌ Province not found")
        return "Not found"

    except Exception as e:
        print(f"Row {index + 1}: ⚠️ Error: {e}")
        return "Error"


# Extract and print progress with province
df['Province'] = [extract_province(row['Google Maps URL'], idx) for idx, row in df.iterrows()]

# Save the result
df.to_excel(OUTPUT_FILE, index=False)
print(f"\n✅ Done! Results saved to {OUTPUT_FILE}")

driver.quit()
