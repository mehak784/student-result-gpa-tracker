from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    semesters = db.relationship('Semester', backref='user', lazy=True)

class Semester(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subjects = db.relationship('Subject', backref='semester', lazy=True)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    credit_hours = db.Column(db.Float)
    marks = db.Column(db.Float)
    grade = db.Column(db.String(5))
    grade_points = db.Column(db.Float)
    semester_id = db.Column(db.Integer, db.ForeignKey('semester.id'))