from dotenv import load_dotenv
import os

load_dotenv()
base_directory = os.path.abspath(os.path.dirname(__file__))


class Config:
    # secret key for forms
    SECRET_KEY = os.getenv("SECRET_KEY")

    # database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(base_directory, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
