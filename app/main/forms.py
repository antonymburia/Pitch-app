from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired,Email


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add more info about you.',validators = [DataRequired()])
    submit = SubmitField('update')

class CommentForm(FlaskForm):
    text = TextAreaField('leave a comment:',validators=[DataRequired()])
    submit = SubmitField('comment')


class PitchForm(FlaskForm):
    title = StringField('Pitch title',validators=[DataRequired()])
    text = TextAreaField('Text',validators=[DataRequired()])
    category = SelectField('Type',choices=[('interview','interview-pitch'),('product','product-pitch'),('motivation', 'motivational-pitch')],validators=[DataRequired()])
    submit = SubmitField('Submit')


