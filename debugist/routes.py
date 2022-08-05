from flask import render_template
from debugist import app, db
from debugist.models import Project, Task


@app.route("/")
def home():
    return render_template("base.html")