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
        if selected_column and keyword:
            col_index = headers.index(selected_column)
            filtered_rows = [
                row for row in rows
                if keyword in row[col_index].lower().replace(' ', '')
            ]

    return render_template(
        'index.html',
        headers=headers,
        rows=filtered_rows,
        selected_column=selected_column,
        keyword=keyword
    )

if __name__ == '__main__':
    app.run(debug=True)
