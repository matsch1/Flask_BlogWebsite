from flask import Blueprint
from flask_wtf import FlaskForm
from flask_login import UserMixin
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length
from dotenv import load_dotenv
import os
from werkzeug.security import generate_password_hash


load_dotenv()

bp = Blueprint('authentication', __name__)

class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


class BlogWriterUser(UserMixin):
    def __init__(self) -> None:
        self.id = os.getenv("USER_BLOG_ID")
        self.name = os.getenv("USER_BLOG_ADMIN")
        self.password_hash = generate_password_hash(os.getenv("USER_BLOG_PW"))
        id = self.id
        name = self.name
        password_hash = self.password_hash

# muss ganz unten stehen
from app.blog.authentication import routes