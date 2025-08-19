from flask import Flask, render_template, request
import csv

app = Flask(__name__)
CSV_FILE = 'data.csv'

def read_csv(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        return list(csv.reader(csvfile))

@app.route('/', methods=['GET', 'POST'])
def index():
    data = read_csv(CSV_FILE)
    headers = data[0]
    rows = data[1:]

    selected_column = ''
    keyword = ''
    filtered_rows = rows

    if request.method == 'POST':
        selected_column = request.form.get('column')
        keyword = request.form.get('keyword', '').lower().replace(' ', '')

        # Define mapping from dropdown value to actual CSV header
        column_mapping = {
            'Brand': headers[0].strip(),     # You can also hardcode it if needed
            'Project': headers[1].strip(),
            'Location': headers[2].strip()
        }

        if selected_column in column_mapping and keyword:
            actual_column_name = column_mapping[selected_column]
            try:
                col_index = headers.index(actual_column_name)
                filtered_rows = [
                    row for row in rows
                    if col_index < len(row) and keyword in (row[col_index] or '').lower().replace(' ', '')
                ]
            except ValueError:
                filtered_rows = []



    return render_template(
        'index.html',
        headers=headers,
        rows=filtered_rows,
        selected_column=selected_column,
        keyword=keyword
    )

if __name__ == '__main__':
    app.run(debug=True)
