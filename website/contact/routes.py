from flask import render_template
from website.contact import bp
from website.models.blog import Blog

@bp.route('/', methods=['GET', 'POST'])
def index():
    about_me = Blog.query.get(1)
    return render_template("contact/index.html", about_me=about_me)
