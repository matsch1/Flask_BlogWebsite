from flask import render_template
from website.contact import bp
from website.models.blog import Blog

ABOUT_ME_ID = 1


@bp.route('/', methods=['GET', 'POST'])
def index():
    about_me = Blog.query.get(ABOUT_ME_ID)
    return render_template("contact/index.html", about_me=about_me)
