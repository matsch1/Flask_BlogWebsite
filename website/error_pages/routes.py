from flask import render_template
from website.error_pages import bp


@bp.app_errorhandler(401)
def unauthorized(e):
    return render_template('error_pages/401.html'), 401


@bp.app_errorhandler(403)
def frobidden(e):
    return render_template('error_pages/403.html'), 403


@bp.app_errorhandler(404)
def not_found_error(e):
    return render_template('error_pages/404.html'), 404


@bp.app_errorhandler(500)
def server_error(e):
    return render_template('error_pages/500.html'), 500
