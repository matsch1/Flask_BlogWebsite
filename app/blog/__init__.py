from flask import Blueprint
from flask_wtf import FlaskForm  # pip install flask-wtf
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, InputRequired, Length
from wtforms.widgets import TextArea



bp = Blueprint('blog', __name__)



class BlogWriterForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = StringField("Content", validators=[
                          DataRequired()], widget=TextArea())
    slug = StringField("Slug", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    submit = SubmitField("Submit")
    logout = SubmitField(label='Logout',render_kw={'formnovalidate': True})





# muss ganz unten stehen
from app.blog import routes