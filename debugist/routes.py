from flask import flash, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from debugist import app, db
from debugist.models import Project, Task, Users


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)


# Projects function. Displays all current projects in alphabetical order.
@app.route("/projects")
def projects():

    if "user" not in session:
        flash("You need to be logged in to view projects")
        return redirect(url_for("home"))

    projects = list(Project.query.order_by(Project.project_name).all())
    return render_template("projects.html", projects=projects)   


# Add Project function. 
@app.route("/add_project", methods=["GET", "POST"])
def add_project():

    if "user" not in session:
        flash("You need to be logged in to add projects")
        return redirect(url_for("home"))

    if request.method == "POST":
        project = Project(project_name=request.form.get("project_name"))
        db.session.add(project)
        db.session.commit()
        return redirect(url_for("projects"))
    return render_template("add_project.html")    


# Edit Project function.
@app.route("/edit_project/<int:project_id>", methods=["GET", "POST"])
def edit_project(project_id):

    if "user" not in session:
        flash("You need to be logged in to edit projects")
        return redirect(url_for("home"))

    project = Project.query.get_or_404(project_id)
    if request.method == "POST":
        project.project_name = request.form.get("project_name")
        db.session.commit()
        return redirect(url_for("projects"))
    return render_template("edit_project.html", project=project)


# Delete Project function.
@app.route("/delete_project/<int:project_id>")
def delete_project(project_id):

    if "user" not in session:
        flash("You need to be logged in to delete projects")
        return redirect(url_for("home"))

    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("projects"))        


# Add Task function.
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if "user" not in session:
        flash("You need to be logged in to add a task")
        return redirect(url_for("home"))

    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            project_id=request.form.get("project_id")
        )
        db.session.add(task)
        db.session.commit()
        flash("Task Successfully Added")
        return redirect(url_for("home"))

    projects = list(Project.query.order_by(Project.project_name).all())    
    return render_template("add_task.html", projects=projects)


# Edit Task function.
@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    projects = list(Project.query.order_by(Project.project_name).all())
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.project_id = request.form.get("project_id")
        db.session.commit()
    return render_template("edit_task.html", task=task, projects=projects)


# Delete Task function.
@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))    


# Adding a user and managing user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in db
        existing_user = Users.query.filter(Users.user_name == \
                                           request.form.get("username").lower()).all()
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        user = Users(
            user_name=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )
        
        db.session.add(user)
        db.session.commit()

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in db
        existing_user = Users.query.filter(Users.user_name == \
                                           request.form.get("username").lower()).all()

        if existing_user:
            print(request.form.get("username"))
            # Ensure hashed password matches user input
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
        
    if "user" in session:
        return render_template("profile.html", username=session["user"])

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))    