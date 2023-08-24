from flask import Blueprint


bp = Blueprint('post', __name__)

# muss ganz unten stehen
from website.blog.post import routes  # NOQA
