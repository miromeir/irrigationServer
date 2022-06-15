from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model, UserMixin):
   id = db.Column('id',db.Integer,primary_key = True)
   name = db.Column(db.String(100))
   password = db.Column(db.String(100))
   topic = db.Column(db.String(1000))
   
   def __init__(self, name, password,topic=""):
      self.name = name
      self.password = password
      self.topic = topic

   def __repr__(self):
      return f'<User:{self.id}>'