from app import db
from models import BlogPost

#create db and db tables
db.create_all()  #init db based on shema on models.py

#insert
db.session.add(BlogPost("kelvin", "looking for a job"))
db.session.add(BlogPost("kipsang", "also looking for a job"))

#commit changes
db.session.commit()