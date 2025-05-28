import pandas as pd
import re
from itertools import zip_longest

# Function to clean a line
def clean_line(line):
    stripped = line.strip()
    if not stripped:
        return ""
    return re.sub(r"\s*\(.*?\)", "", stripped)

# Read and clean all files
with open("data.txt", encoding="utf-8") as f1:
    col1 = [clean_line(line) for line in f1.readlines()]

with open("data2.txt", encoding="utf-8") as f2:
    col2 = [clean_line(line) for line in f2.readlines()]

with open("data3.txt", encoding="utf-8") as f3:
    col3 = [clean_line(line) for line in f3.readlines()]

# Use zip_longest to pad shorter columns with blank entries
rows = list(zip_longest(col1, col2, col3, fillvalue=""))

# Create DataFrame and export to Excel
df = pd.DataFrame(rows, columns=["Column1", "Column2", "Column3"])
df.to_excel("Oh! Juice.xlsx", index=False)
