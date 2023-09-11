from flask import render_template, request
from sqlalchemy import desc, func
from flask_login import login_required

from website.blog import bp
from website.models.blog import Blog
from config import Config

app_config = Config()


@bp.route('/page=<page_number>', methods=['GET', 'POST'])
def index(page_number=1):
    posts = Blog.query.order_by(desc(Blog.date_posted))

    items_per_page = app_config.ITEMS_PER_PAGE
    max_number_of_pages = int(
        str(posts.count()/items_per_page).split('.')[0])+1

    if page_number == 1:
        selected_posts = posts[:items_per_page]
    elif int(page_number) >= max_number_of_pages:
        start_pos = 0 if page_number == 1 else items_per_page * \
            (int(page_number) - 1)
        selected_posts = posts[start_pos:]
    else:
        start_pos = 0 if page_number == 1 else items_per_page * \
            (int(page_number) - 1)
        selected_posts = posts[start_pos: start_pos + items_per_page]

    return render_template("blog/index.html", posts=selected_posts, page_number=int(page_number), max_number_of_pages=max_number_of_pages)


@bp.route('/posts_edit', methods=['GET', 'POST'])
@login_required
def posts_edit():
    posts = Blog.query.order_by(desc(Blog.date_posted))
    return render_template("blog/posts_edit.html", posts=posts, page_number=1, max_number_of_pages=1)


@bp.route('/cat=<categorie>', methods=['GET', 'POST'])
def categorie(categorie):
    posts = Blog.query.filter(Blog.categories.contains(categorie))
    # catgegorie=categorie kann wahrscheinlich gelöscht werden
    return render_template("blog/categorie.html", posts=posts, categorie=categorie, page_number=1, max_number_of_pages=1)


@bp.route('/search', methods=['POST'])
def search():
    for key, value in request.form.items():
        if key == "Search":
            posts = Blog.query.filter(Blog.content.ilike(f'%{value}%'))

            return render_template("blog/search.html", posts=posts, page_number=1, max_number_of_pages=1)


@bp.app_template_filter('formatdatetime')
def format_datetime(value, format="%d. %b %Y - %H:%M"):
    if value is None:
        return ""
    return value.strftime(format)
