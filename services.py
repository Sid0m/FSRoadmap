import csv

#file_path = "static/csv/futureskills_ks.csv"
file_path = "static/csv/futureskills_bs.csv"

def read_csv():
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                'id': row['id'],
                'title': row['skill'],
                'definition': row['definition'],
                'small_story': row['small_story'],
                'big_story': row['big_story']
                })
    return data

