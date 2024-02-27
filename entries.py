from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)

class Entries(db.Model):
    entriesID = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(50)) 
    message = db.Column(db.String(10000))