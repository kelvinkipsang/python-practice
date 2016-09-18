from app import db

class BlogPost(db.model):
    __tablename__ = "posts"

    Id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=)

    def __init__(self,title,description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '<title{}'.format(self.title)