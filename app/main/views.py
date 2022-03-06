from . import main
from flask_login import login_required,current_user
from .forms import UpdateProfile, PitchForm,CommentForm
from flask import render_template,redirect,url_for,abort,request
from ..models import User,Pitch,Comment
from .. import db


#Views
@main.route('/')
def index():
    '''
    view to load index.html
    '''

    #get pitch by category

    pitches = Pitch.query.all()
    

    return render_template('index.html', pitches = pitches)
    
    


@main.route('/pitches/product_pitches')
def product_pitches():
    

    pitches = Pitch.get_pitches('product')

    return pitches

@main.route('/pitches/promotion_pitches')
def promotion_pitches():

    pitches = Pitch.get_pitches('promotion')

    return pitches

@main.route('/pitches/interview_pitches')
def interview_pitches():

    pitches = Pitch.get_pitches('interview')
    return pitches

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
        add_description = pitch_form.add_description.data
        pitch = pitch_form.pitch_content.data
        category = pitch_form.category.data

        # Updated pitch instance
        new_pitch = Pitch(add_description=add_description,content=pitch,category=category,user=current_user,likes=0,dislikes=0)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    
    return render_template('newpitch.html',pitch_form = pitch_form )


