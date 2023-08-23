from flask import Blueprint

bp = Blueprint('contact', __name__)

# muss ganz unten stehen
from website.contact import routes  # NOQA
