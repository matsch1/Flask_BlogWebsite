from flask import render_template, redirect, flash, url_for, request
from flask_login import login_required, logout_user
from datetime import datetime

from website.blog import BlogWriterForm
from website.blog.post import bp
from website.models.blog import Blog
from website.extensions import db


@bp.route('/<slug>_<id>', methods=['GET', 'POST'])
def show(slug, id):
    post = Blog.query.get(id)
    if post.categories:
        categories_array = __convert_string_to_array__(post.categories)
    if post.images:
        images_array = __convert_array_to_string__(post.images)
    return render_template("blog/post/show.html", post=post, categories=categories_array, images=images_array)


@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BlogWriterForm()

    if form.validate_on_submit():
        categories_string = __convert_dbColum_to_string(form.categories)
        for imageID in form.imageIDs:
            if imageID.data:
                imageID.data = 'https://drive.google.com/uc?id=' + imageID.data
        images_string = __convert_dbColum_to_string(form.imageIDs)

        post = Blog(title=form.title.data,
                    content=form.content.data, slug=form.slug.data, categories=categories_string, images=images_string,
                    author=form.author.data, date_posted=datetime.now())
        form.title.data = ""
        form.content.data = ""
        form.slug.data = ""

        db.session.add(post)
        db.session.commit()
        flash("Blog Post Submitted Successfully")

    if request.method == 'POST' and form.logout.data:
        logout_user()
        return redirect(url_for('blog.index', page_number=1))

    return render_template("blog/post/add.html", form=form)


@bp.route('/edit/<slug>_<id>', methods=['GET', 'POST'])
def edit(id, slug):
    post = Blog.query.get(id)

    images_array = __convert_string_to_array__(post.images)
    for index, image in enumerate(images_array):
        url_split = image.split('=')
        images_array[index] = url_split[-1]

    form = BlogWriterForm(title=post.title, slug=post.slug,
                          author=post.author, content=post.content, categories=__convert_string_to_array__(post.categories), imageIDs=images_array)

    if form.submit.data:  # ignore logout
        categories_array = []
        for categorie in form.categories:
            categories_array.append(categorie.data)
        categories_string = __convert_array_to_string__(categories_array)
        setattr(post, 'categories', categories_string)
        for imageID in form.imageIDs:
            if imageID.data:
                imageID.data = 'https://drive.google.com/uc?id=' + imageID.data
        images_string = __convert_dbColum_to_string(form.imageIDs)
        setattr(post, 'images', images_string)
        setattr(post, 'title', form.title.data)
        setattr(post, 'content', form.content.data)
        setattr(post, 'slug', form.slug.data)

        db.session.commit()

        flash("Blog Post Updated Successfully")

    if request.method == 'POST' and form.logout.data:
        logout_user()
        return redirect(url_for('blog.index', page_number=1))
    return render_template("blog/post/edit.html", form=form)


def __convert_dbColum_to_string(dbColum):
    array = []
    for item in dbColum:
        if item.data:
            array.append(item.data)
            item.data = ""
    return __convert_array_to_string__(array)


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
