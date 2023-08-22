from flask import render_template
from website.main import bp
from website.models.blog import Blog


@bp.route('/')
def index():
    post = Blog.query.get(4)
    return render_template('index.html', post=post)
