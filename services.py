import csv

file_path = "static/csv/futureskills.csv"

def read_csv():
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                'title': row['skill'],
                'definition': row['definition'],
                'story': row['story']
                })
    return data

