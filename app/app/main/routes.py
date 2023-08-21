from flask import render_template
from app.main import bp
from app.models.blog import Blog


@bp.route('/')
def index():
    post = Blog.query.get(4)
    return render_template('index.html', post=post)
