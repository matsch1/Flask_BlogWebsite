from flask import render_template
from sqlalchemy import desc

from website.main import bp
from website.models.blog import Blog
from config import Config

app_config = Config()


@bp.route('/')
def index(page_number=1):
    posts = Blog.query.order_by(desc(Blog.date_posted))
    items_per_page = app_config.ITEMS_PER_PAGE
    max_number_of_pages = int(
        str(posts.count()/items_per_page).split('.')[0])+1
    selected_posts = posts[:items_per_page]

    return render_template("blog/index.html", posts=selected_posts, page_number=int(page_number), max_number_of_pages=max_number_of_pages)
