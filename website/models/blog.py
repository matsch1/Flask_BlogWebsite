from datetime import datetime
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
        content_html = markdown(value, extensions=['fenced_code', TocExtension(baselevel=3),
                                                   'codehilite', 'meta', 'tables'], output_format="html5")

        target.content_html = change_html_style(content_html)

    def __repr__(self):
        return f'<Titel {self.title}>'


db.event.listen(Blog.content, 'set', Blog.on_changed_content)


def change_html_style(content_html):
    # change link color
    styled_content = content_html.replace(
        '<a href', '<a class="dark_link" href')
    styled_content = open_links_in_new_tab(styled_content)

    return styled_content


def open_links_in_new_tab(content_html):
    split_string = '<h4 id="introduction">Introduction</h4>'
    if split_string in content_html:
        content_split = content_html.split(
            split_string)
        content_without_toc = split_string+content_split[1]
        styled_content = content_without_toc.replace(
            '<a class="dark_link" href', '<a class="dark_link" target="_blank" href')
        return content_split[0] + styled_content
    else:
        return content_html
