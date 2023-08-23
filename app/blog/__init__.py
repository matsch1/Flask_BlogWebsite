from flask import Blueprint
from flask_wtf import FlaskForm  # pip install flask-wtf
from wtforms import StringField, FieldList, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length
from wtforms.widgets import TextArea
from flask_pagedown.fields import PageDownField


bp = Blueprint('blog', __name__)


class BlogWriterForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = PageDownField('Enter Your Markdown', validators=[DataRequired()])
    slug = StringField("Slug", validators=[DataRequired()])
    author = StringField("Author", validators=[
                         DataRequired()], default="Matthias Schäfer")
    categories = FieldList(StringField("Categorie"), min_entries=3)
    submit = SubmitField("Post")
    logout = SubmitField(label='Logout', render_kw={'formnovalidate': True})


# muss ganz unten stehen
from app.blog import routes  # NOQA
