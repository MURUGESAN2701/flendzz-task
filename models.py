from flask_sqlalchemy import SQLAlchemy
from datetime  import date

db = SQLAlchemy()

class students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    roll_no = db.Column(db.String(50), unique=True, nullable =False)
    name = db.Column(db.String(255), nullable = False )
    dob = db.Column(db.Date , nullable = False)
    marks = db.relationship('Mark', backref='students', lazy=True)

    def  __init__(self, dob, name, roll_no):
        self.dob = dob
        self.name = name
        self.roll_no = roll_no
    

class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    marks = db.Column(db.Integer)

    def __init__(self, student_id, marks):
        self.student_id = student_id
        self.marks = marks
