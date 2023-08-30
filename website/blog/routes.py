from flask import render_template
from sqlalchemy import desc
from flask_login import login_required

from website.blog import bp
from website.models.blog import Blog


@bp.route('/', methods=['GET', 'POST'])
def index():
    posts = Blog.query.order_by(desc(Blog.date_posted))
    return render_template("blog/index.html", posts=posts)


@bp.route('/posts_edit', methods=['GET', 'POST'])
@login_required
def posts_edit():
    posts = Blog.query.order_by(desc(Blog.date_posted))
    return render_template("blog/posts_edit.html", posts=posts)


@bp.route('/<categorie>', methods=['GET', 'POST'])
def categorie(categorie):
    posts = Blog.query.filter(Blog.categories.contains(categorie))
    return render_template("blog/categorie.html", posts=posts, categorie=categorie)


@bp.app_template_filter('formatdatetime')
def format_datetime(value, format="%d. %b %Y - %H:%M"):
    if value is None:
        return ""
    return value.strftime(format)
