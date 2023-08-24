from flask import Blueprint

bp = Blueprint('main', __name__)


# muss ganz unten stehen
from website.main import routes  # NOQA
