from flask import render_template, redirect, flash, url_for, request, current_app
from sqlalchemy import desc, literal
from flask_login import login_required, logout_user
from datetime import datetime

from app.blog import bp, BlogWriterForm
from app.models.blog import Blog
from app.extensions import db


@bp.route('/', methods=['GET', 'POST'])
def index():
    posts = Blog.query.order_by(desc(Blog.date_posted))
    # for post in posts:
    #     if post.categories:
    #         current_app.logger.info(post.categories)
    #         categories_array = __convert_string_to_array__(post.categories)
    #         post.categories = categories_array
    #         current_app.logger.info(post.categories)
    return render_template("blog/index.html", posts=posts)


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BlogWriterForm()

    if form.validate_on_submit():
        categories_array = []
        for categorie in form.categories:
            categories_array.append(categorie.data)
            categorie.data = ""
        categories_string = __convert_array_to_string__(categories_array)

        post = Blog(title=form.title.data,
                    content=form.content.data, slug=form.slug.data, categories=categories_string,
                    author=form.author.data, date_posted=datetime.now())
        form.title.data = ""
        form.content.data = ""
        form.slug.data = ""

        db.session.add(post)
        db.session.commit()
        flash("Blog Post Submitted Successfully")

    if request.method == 'POST' and form.logout.data:
        logout_user()
        return redirect(url_for('blog.index'))

    return render_template("blog/add.html", form=form)


@bp.route('/post/<slug>_<id>', methods=['GET', 'POST'])
def post(id, slug):
    post = Blog.query.get(id)
    if post.categories:
        categories_array = __convert_string_to_array__(post.categories)
    return render_template("blog/post.html", post=post, categories=categories_array)


@bp.route('/<categorie>', methods=['GET', 'POST'])
def categorie(categorie):
    posts = Blog.query.filter(Blog.categories.contains(categorie))
    # current_app.logger.info(posts)
    for post in posts:
        current_app.logger.info(post.content_html)
    return render_template("blog/categorie.html", posts=posts, categorie=categorie)


@bp.app_template_filter('formatdatetime')
def format_datetime(value, format="%d. %b %Y - %H:%M"):
    if value is None:
        return ""
    return value.strftime(format)


def __convert_array_to_string__(array):
    array_string = array[0]
    for index, element in enumerate(array):
        if index > 0 and index:
            array_string = array_string + ',' + element
    return array_string[:-1]


def __convert_string_to_array__(string):
    array = string.split(',')
    return array
