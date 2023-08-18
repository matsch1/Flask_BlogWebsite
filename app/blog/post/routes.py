from flask import render_template, redirect, flash, url_for, request, current_app
from flask_login import login_required, logout_user
from datetime import datetime

from app.blog import BlogWriterForm
from app.blog.post import bp
from app.models.blog import Blog
from app.extensions import db


@bp.route('/<slug>_<id>', methods=['GET', 'POST'])
def show(slug, id):
    post = Blog.query.get(id)
    if post.categories:
        categories_array = __convert_string_to_array__(post.categories)
    return render_template("blog/post/show.html", post=post, categories=categories_array)


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

    return render_template("blog/post/add.html", form=form)


@bp.route('/edit/<slug>_<id>', methods=['GET', 'POST'])
def edit(id, slug):
    post = Blog.query.get(id)

    form = BlogWriterForm(title=post.title, slug=post.slug,
                          author=post.author, content=post.content, categories=__convert_string_to_array__(post.categories))

    if form.validate_on_submit():
        # current_app.logger.info('Submit pressed')
        categories_array = []
        for categorie in form.categories:
            categories_array.append(categorie.data)
        categories_string = __convert_array_to_string__(categories_array)
        setattr(post, 'title', form.title.data)
        setattr(post, 'content', form.content.data)
        setattr(post, 'slug', form.slug.data)
        setattr(post, 'categories', categories_string)
        db.session.commit()

        flash("Blog Post Updated Successfully")

    if request.method == 'POST' and form.logout.data:
        logout_user()
        return redirect(url_for('blog.index'))
    return render_template("blog/post/edit.html", form=form)


def __convert_array_to_string__(array):
    array_string = array[0]
    for index, element in enumerate(array):
        if index > 0 and index:
            if len(element) > 0:
                array_string = array_string + ',' + element
    return array_string


def __convert_string_to_array__(string):
    array = string.split(',')
    return array
