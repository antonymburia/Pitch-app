from . import main
from flask_login import login_required,current_user
from .forms import UpdateProfile, PitchForm,CommentForm
from flask import render_template,redirect,url_for,abort
from ..models import User,Pitch,Comment
from .. import db,photos


#Views
@main.route('/')
def index():
  '''
  view to load index.html
  '''

  #get pitch by category

  product_piches = Pitch.get_pitches('product')
  interview_piches = Pitch.get_pitches('interview')
  motivation_pitches = Pitch.get_pitches('motivation')

  return render_template('index.html', interview = interview_piches, product = product_piches, motivation = motivation_pitches)


