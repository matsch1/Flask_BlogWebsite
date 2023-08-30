from flask import Blueprint
from flask_wtf import FlaskForm  # pip install flask-wtf
from wtforms import StringField, FieldList, SubmitField, TextAreaField
from wtforms.validators import DataRequired

bp = Blueprint('blog', __name__)


class BlogWriterForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField('Enter Your Markdown', render_kw={
                            "rows": 70, "cols": 11})
    slug = StringField("Slug", validators=[DataRequired()])
    author = StringField("Author", validators=[
                         DataRequired()], default="Matthias Schäfer")
    categories = FieldList(StringField("Categorie"), min_entries=3)
    imageIDs = FieldList(StringField("ImageID"), min_entries=3)
    submit = SubmitField("Post")
    logout = SubmitField(label='Logout', render_kw={'formnovalidate': True})


# muss ganz unten stehen
from website.blog import routes  # NOQA
