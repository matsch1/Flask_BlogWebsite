from datetime import datetime
import bleach
from markdown import markdown

from app.extensions import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    content_html = db.Column(db.Text)
    author = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(
        db.DateTime, default=datetime.now())
    slug = db.Column(db.String(255))
    categories = db.Column(db.String(100), nullable=True)

    @staticmethod
    def on_changed_content(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                        'h1', 'h2', 'h3', 'p', 'Img']
        # target.content_html = bleach.linkify(bleach.clean(
        #     markdown(value, output_format='html'),
        #     tags=allowed_tags, strip=True))
        target.content_html = bleach.linkify(
            markdown(value, output_format='html'))

    def __repr__(self):
        return f'<Titel {self.title}>'


db.event.listen(Blog.content, 'set', Blog.on_changed_content)
