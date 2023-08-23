from flask import Blueprint

bp = Blueprint('contact', __name__)

# muss ganz unten stehen
from app.contact import routes  # NOQA
