from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


# database
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text)
    author = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    slug = db.Column(db.String(255))

    def __repr__(self):
        return f'<Titel {self.title}>'

@app.route('/') # for blog posts
def index():
    return render_template("index.html")

@app.route('/android_apps')
def android_apps():
    return render_template("android_apps.html")

@app.route('/books')
def books():
    return render_template("books.html")


if __name__ == '__main__':
    app.run(debug=True)