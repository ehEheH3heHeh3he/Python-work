import pandas as pd
import re

# Read input from .txt
with open("Chatramue.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

# Process each line
rows = []
for line in lines:
    match = re.search(r'(?i)\b(floor\s*\w+|fl\.\s*\w+)\b', line)
    if match:
        floor_info = match.group(0).strip()
        name = re.sub(re.escape(floor_info), '', line, flags=re.IGNORECASE).strip()
    else:
        floor_info = ""
        name = line
    rows.append([name, floor_info])

# Export to Excel
df = pd.DataFrame(rows, columns=["Name", "Floor"])
df.to_excel("chatramues.xlsx", index=False)
