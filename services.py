import csv
import pandas as pd

file_path_story = "static/csv/futureskills_bs.csv"
file_path_data = "static/csv/futureskills.csv"

def read_csv_story():
    data = []
    with open(file_path_story, 'r', encoding='utf-8') as file:
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

def read_csv_data():
    data = []
    with open(file_path_data, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                #'id': row['id'],
                'count': row['count'],
                'skill': row['skill']
                })
    return data