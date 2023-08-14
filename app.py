from flask import Flask, render_template, flash
from flask_wtf import FlaskForm  # pip install flask-wtf
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from flask_sqlalchemy import SQLAlchemy  # pip install Flask-SQLAlchemy
from sqlalchemy import desc
from datetime import datetime
import os
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()
app = Flask(__name__)

folder_directory = os.path.abspath(os.path.dirname(__file__))

# secret key for forms
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") or ""

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(folder_directory, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    author = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(
        db.DateTime, default=datetime.utcnow())
    slug = db.Column(db.String(255))

    def __repr__(self):
        return f'<Titel {self.title}>'


class BlogWriterForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = StringField("Content", validators=[
                          DataRequired()], widget=TextArea())
    slug = StringField("Slug", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')  # for blog posts
def index():
    posts = Blog.query.order_by(desc(Blog.date_posted))

    return render_template("index.html", posts=posts)


@app.route('/android_apps')
def android_apps():
    return render_template("android_apps.html")


@app.route('/books')
def books():
    return render_template("books.html")


@app.route('/add-post', methods=['GET', 'POST'])
def add_post():
    form = BlogWriterForm()

    if form.validate_on_submit():
        post = Blog(title=form.title.data,
                    content=form.content.data, slug=form.slug.data,
                    author=form.author.data)
        form.title.data = ""
        form.content.data = ""
        form.slug.data = ""
        form.author.data = ""
        print("data cleared")
        db.session.add(post)
        db.session.commit()
        print("data stored")
        flash("Blog Post Submitted Successfully")

    return render_template("blog_input.html", form=form)


@app.template_filter('formatdatetime')
def format_datetime(value, format="%d. %b %Y - %I:%M"):
    """Format a date time to (Default): d Mon YYYY HH:MM"""
    if value is None:
        return ""
    return value.strftime(format)


if __name__ == '__main__':
    app.run(debug=True)
