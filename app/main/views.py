from . import main
from flask_login import login_required,current_user
from .forms import UpdateProfile, PitchForm,CommentForm
from flask import render_template,redirect,url_for,abort,request,flash
from ..models import User,Pitch,Comment
from .. import db


#Views
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    view to load index.html
    '''

    
    
    
    pitches = Pitch.query.all()
    pitch = Pitch.query.filter_by(id=Pitch.id).first()
    
    name =  User.query.filter_by(id =pitch.user_id).first()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data
        new_comment = Comment(comment = comment,user_id = current_user, pitch = pitch)
        new_comment.save_comment()
        
        flash('Your comment has been submitted')
        return redirect(url_for('.index'))

    
    

    return render_template('index.html', pitches = pitches, name = name, comment_form = comment_form)
    

@main.route('/user/<usersname>')
def profile(usersname):
    user = User.query.filter_by(username = usersname).first()
    user_joined = user.date_joined.strftime('%b %d, %Y')
    pitches = Pitch.query.filter_by(user_id=Pitch.user_id).all()

    if user is None:
        abort(404)
        

    

    return render_template("profile/profile.html", user = user, date = user_joined, pitches = pitches)

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

@main.route('/category/')
def category():
    interview_pitches = Pitch.query.filter_by(category='interview').all()
    product_pitches = Pitch.query.filter_by(category='product').all()
    promotion_pitches = Pitch.query.filter_by(category='promotion').all()
    


    return render_template('category.html', interview = interview_pitches, product = product_pitches, promotion = promotion_pitches)

@main.route('/comments/')
def comments():
    pitch = Pitch.query.filter_by(id=Pitch.id).first()
    comments = Comment.get_comments(pitch)
    name = User.query.filter_by(id = Comment.pitch).first()

    return render_template('comments.html', comments = comments, name = name)

