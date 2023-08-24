from flask import render_template
from sqlalchemy import desc

from website.main import bp
from website.models.blog import Blog
from website.extensions import count_lines


@bp.route('/')
def index():
    posts = Blog.query.order_by(desc(Blog.date_posted))

    return render_template("index.html", posts=posts)
