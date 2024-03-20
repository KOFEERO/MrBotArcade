from flask_login import UserMixin
from .utils.db import db
from datetime import datetime

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Arcade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    ip = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    imagen = db.Column(db.String(100), nullable=True)
    date_joined = db.Column(db.DateTime, default=datetime.now())  



class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee = db.relationship('Employee', backref='time', lazy=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)

    machine = db.relationship('Arcade', backref='time', lazy=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('arcade.id'), nullable=False)

    description = db.Column(db.Text, nullable=True)
    hour = db.Column(db.Integer, nullable=False)
    minute = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.now()) 


class Reset(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    employee = db.relationship('Employee', backref='reset', lazy=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)

    machine = db.relationship('Arcade', backref='reset', lazy=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('arcade.id'), nullable=False)
    time_reset = db.Column(db.String(5), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.now()) 