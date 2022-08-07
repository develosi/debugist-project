from flask import render_template
from debugist import app, db
from debugist.models import Project, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")    