import pandas as pd
from google.cloud import translate_v2 as translate
from tqdm import tqdm  # For progress bar, install with: pip install tqdm

# Initialize Google Translate client
translate_client = translate.Client()

# Dictionary of Thai abbreviations to full forms
REPLACEMENTS = {
    'รพ.': 'โรงพยาบาล',
    'ม.': 'มหาวิทยาลัย',
    'รร.': 'โรงแรม',
    'ปตท.': 'สถานีบริการน้ำมัน ปตท.',
    'สน.': 'สถานีตำรวจ',
    'ศูนย์ฯ': 'ศูนย์',
    # Add more rules here if needed
}

def preprocess_thai_name(text):
    if pd.isna(text):
        return text
    for abbr, full in REPLACEMENTS.items():
        text = text.replace(abbr, full)
    return text

def translate_text(text):
    if pd.isna(text) or not text.strip():
        return text
    text = preprocess_thai_name(text)
    try:
        result = translate_client.translate(text, source_language='th', target_language='en')
        return result['translatedText']
    except Exception as e:
        print(f"Translation error for '{text}': {e}")
        return text

def batch_translate(series, batch_size=100):
    translated_texts = []
    for i in tqdm(range(0, len(series), batch_size), desc="Translating"):
        batch = series.iloc[i:i+batch_size].tolist()
        batch_translated = [translate_text(item) for item in batch]
        translated_texts.extend(batch_translated)
    return translated_texts

def main():
    # Load your Excel file
    df = pd.read_excel("Work copy.xlsx")

    # Strip spaces from column names (helps avoid key errors)
    df.columns = df.columns.str.strip()
    print("Columns found:", df.columns.tolist())

    # TODO: Replace 'PlaceName' with the actual column name after checking printed columns
    source_col = "Project"  # example placeholder

    if source_col not in df.columns:
        print(f"Error: Column '{source_col}' not found in the Excel file.")
        return

    # Translate the column
    df[source_col + '_EN'] = batch_translate(df[source_col])

    # Save to new Excel file
    df.to_excel("translated_places.xlsx", index=False)
    print("Translation complete. Saved to 'translated_places.xlsx'.")

if __name__ == "__main__":
    main()
