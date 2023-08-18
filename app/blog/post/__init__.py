from flask import Blueprint


bp = Blueprint('post', __name__)

# muss ganz unten stehen
from app.blog.post import routes  # NOQA
