from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import login_manager


class User(db.Model):
  __tablename__ = 'users'
  id =db.Column(db.Integer,primary_key =True)
  username = db.Column(db.string(255))  

  def __repr__(self):
    return f'User {self.username}'


class Pitch(db.Model):
  __tablename__ = "pitches"

  id = db.Column(db.Integer,primary_key = True)
  pitch_title = db.Column(db.String)
  pitch_content = db.Column(db.String(1000))
  category = db.Column(db.String)
  posted = db.Column(db.DateTime,default=datetime.utcnow)
  user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
  likes = db.Column(db.Integer)
  dislikes = db.Column(db.Integer)


  comments = db.relationship('Comment',backref =  'pitch_id',lazy = "dynamic")

  def save_pitch(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_pitches(cls,category):
    pitches = Pitch.query.filter_by(category=category).all()
    return pitches

  @classmethod
  def get_pitch(cls,id):
    pitch = Pitch.query.filter_by(id=id).first()

    return pitch

class Comment(db.Model):

  __tablename__ = 'comments'
  id = db.Column(db.Integer,primary_key = True)
  comment = db.Column(db.String(500))
  user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
  pitch = db.Column(db.Integer,db.ForeignKey("pitches.id"))

  

  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,pitch):
    comments = Comment.query.filter_by(pitch_id=pitch).all()
    return comments