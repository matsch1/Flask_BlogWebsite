from flask import Blueprint

bp = Blueprint('error_pages', __name__)

# muss ganz unten stehen
from website.error_pages import routes  # NOQA
