from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required
from werkzeug.security import check_password_hash

from website.authentication import bp
from website.authentication import LoginForm, BlogWriterUser


@bp.route('/', methods=['GET', 'POST'])
def index():
    user = BlogWriterUser()
    form = LoginForm()

    if form.validate_on_submit():
        if user.name == form.username.data and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            if request.args.get("next") is not None:
                if 'add' in request.args.get("next"):
                    return redirect(url_for('blog.add'))
                elif 'edit' in request.args.get("next"):
                    return redirect(url_for('blog.edit'))
            else:
                return redirect(url_for('authentication.user_sites'))
        else:
            flash('Invalid User')
            redirect(url_for('authentication.index'))
    return render_template("authentication/index.html", form=form)


@bp.route('/user_sites', methods=['GET', 'POST'])
@login_required
def user_sites():
    return render_template("authentication/user_sites.html")
