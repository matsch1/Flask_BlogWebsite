from flask import render_template, redirect, url_for,flash
from flask_login import login_user
from werkzeug.security import check_password_hash

from app.blog.authentication import bp
from app.blog.authentication import LoginForm, BlogWriterUser

@bp.route('/', methods=['GET', 'POST'])
def index():
    user = BlogWriterUser()
    form = LoginForm()

    if form.validate_on_submit():
        if user.name == form.username.data and check_password_hash(user.password_hash,form.password.data):
            login_user(user)
            return redirect(url_for('blog.add'))
        else:
            flash('Invalid User')
            redirect(url_for('blog.authentication.index'))
    return render_template("blog/authentication/index.html", form = form)
