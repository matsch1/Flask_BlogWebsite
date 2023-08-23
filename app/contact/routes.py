from flask import render_template
from sqlalchemy import desc
from app.contact import bp
from app.models.blog import Blog


@bp.route('/', methods=['GET', 'POST'])
def index():
    about_me = Blog.query.get(4)
    return render_template("contact/index.html", about_me=about_me)
