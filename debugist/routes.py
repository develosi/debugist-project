from flask import render_template
from debugist import app, db
from debugist.models import Project, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")    


@app.route("/add_project", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        project = Project(project_name=request.form.get("project_name"))
        db.session.add(project)
        db.session.commit()
        return redirect(url_for("projects"))
    return render_template("add_project.html")    