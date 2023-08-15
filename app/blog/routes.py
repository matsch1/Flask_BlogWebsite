from flask import render_template, redirect, flash, url_for, request
from sqlalchemy import desc
from flask_login import login_user, login_required, logout_user

from app.blog import bp, BlogWriterForm
from app.models.blog import Blog
from app.extensions import db


@bp.route('/', methods=['GET', 'POST'])
def index():
    posts = Blog.query.order_by(desc(Blog.date_posted))

    return render_template("blog/index.html" , posts=posts)


@bp.route('/add', methods=['GET', 'POST'])
# @login_required
def add_post():
    form = BlogWriterForm()

    if form.validate_on_submit():
        post = Blog(title=form.title.data,
                    content=form.content.data, slug=form.slug.data,
                    author=form.author.data)
        form.title.data = ""
        form.content.data = ""
        form.slug.data = ""
        form.author.data = ""
        db.session.add(post)
        db.session.commit()
        flash("Blog Post Submitted Successfully")


    return render_template("blog/add.html", form=form)


@bp.app_template_filter('formatdatetime')
def format_datetime(value, format="%d. %b %Y - %I:%M"):
    """Format a date time to (Default): d Mon YYYY HH:MM"""
    if value is None:
        return ""
    return value.strftime(format)


