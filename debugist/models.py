from debugist import db


class Project(db.Model):
    # schema for Projects model
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(50), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="Project", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ represents itself in the form of a string
        return self.project_name


class Task(db.Model):
    # schema for Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(80), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ represents itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )