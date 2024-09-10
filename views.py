from flask import Blueprint, render_template
from services import *

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    skills = read_csv()
    return render_template("index.html", skills=skills)