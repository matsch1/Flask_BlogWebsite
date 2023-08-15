from app.extensions import db
from datetime import datetime


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
