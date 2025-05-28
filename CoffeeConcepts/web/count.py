import csv
from collections import Counter

# Read the CSV and count first column values
with open('data.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    first_col = [row[0] for row in reader if row]  # row[0] is the first column

counts = Counter(first_col)

# Show only duplicates
duplicates = {item: count for item, count in counts.items() if count > 1}

print(duplicates)
