from flask import render_template
from sqlalchemy import desc
from dataclasses import dataclass


from app.main import bp
from app.models.blog import Blog
from app.extensions import count_lines


@bp.route('/')
def index():
    posts = Blog.query.order_by(desc(Blog.date_posted))
    number_of_lines = count_lines()

    return render_template("index.html", posts=posts, number_of_lines=number_of_lines)
