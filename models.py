from app import db
from flask_sqlalchemy import SQLAlchemy

class BlogPost(db.Model):
    __tablename__ = "posts"

    Id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self,title,description): #constructor for each indiv instance attribute
        self.title = title
        self.description = description

    def __repr__(self): #specify how u want the object to be repd when printed
        return '<{}>'.format(self.title)