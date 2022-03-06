from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add more info about you.',validators = [DataRequired()])
    submit = SubmitField('update')

class CommentForm(FlaskForm):
    text = TextAreaField('leave a comment below:',validators=[DataRequired()])
    submit = SubmitField('comment')


class PitchForm(FlaskForm):
    pitch_content = TextAreaField('Pitch Content',validators=[DataRequired()])
    add_description = StringField('Pitch description',validators=[DataRequired()])
    category = SelectField('Type',choices=[('interview'),('promotion'),('product')],validators=[DataRequired()])
    submit = SubmitField('Submit')


