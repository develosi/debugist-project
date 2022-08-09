from flask import render_template, request, redirect, url_for
from debugist import app, db
from debugist.models import Project, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/projects")
def projects():
    projects = list(Project.query.order_by(Project.project_name).all())
    return render_template("projects.html", projects=projects)   


@app.route("/add_project", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        project = Project(project_name=request.form.get("project_name"))
        db.session.add(project)
        db.session.commit()
        return redirect(url_for("projects"))
    return render_template("add_project.html")    


@app.route("/edit_project/<int:project_id>", methods=["GET", "POST"])
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == "POST":
        project.project_name = request.form.get("project_name")
        db.session.commit()
        return redirect(url_for("projects"))
    return render_template("edit_project.html", project=project)


@app.route("/delete_project/<int:project_id>")
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("projects"))        