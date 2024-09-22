from flask import Blueprint, render_template
from services import *

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    skills = read_csv_story()
    return render_template("index.html", skills=skills)

@views.route("/jobanalysis")
def jobs():
    data = read_csv_data()
    labels = [row['skill'] for row in data]
    values = [row['count'] for row in data]
    return render_template("plot.html", labels=labels, values=values)