from flask import Blueprint
from flask_wtf import FlaskForm  # pip install flask-wtf
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, InputRequired, Length
from wtforms.widgets import TextArea
from flask_pagedown.fields import PageDownField


bp = Blueprint('blog', __name__)


class BlogWriterForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    # content = StringField("Content", validators=[
    #                       DataRequired()], widget=TextArea())
    content = PageDownField('Enter Your Markdown', validators=[DataRequired()])
    slug = StringField("Slug", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    submit = SubmitField("Submit")
    logout = SubmitField(label='Logout', render_kw={'formnovalidate': True})


# muss ganz unten stehen
from app.blog import routes  # NOQA
