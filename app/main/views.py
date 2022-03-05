from . import main
from flask_login import login_required,current_user
from .forms import UpdateProfile, PitchForm,CommentForm
from flask import render_template,redirect,url_for,abort,request
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
@main.route('/user/<usersname>')
def profile(usersname):
    user = User.query.filter_by(username = usersname).first()
    user_joined = user.date_joined.strftime('%b %d, %Y')

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, date = user_joined)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.text.data
        category = pitch_form.category.data

        # Updated pitch instance
        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,user=current_user,likes=0,dislikes=0)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    
    return render_template('new_pitch.html',pitch_form = pitch_form )


