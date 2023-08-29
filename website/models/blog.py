from datetime import datetime
import bleach
from markdown import markdown
from markdown.extensions.toc import TocExtension

from website.extensions import db


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
    images = db.Column(db.Text, nullable=True)

    @staticmethod
    def on_changed_content(target, value, oldvalue, initiator):
        target.content_html= markdown(value, extensions=['fenced_code', TocExtension(baselevel=3),
			'codehilite', 'meta', 'tables'], output_format="html5")

    def __repr__(self):
        return f'<Titel {self.title}>'


db.event.listen(Blog.content, 'set', Blog.on_changed_content)
