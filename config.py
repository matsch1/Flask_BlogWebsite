from dotenv import load_dotenv
import os

load_dotenv()
base_directory = os.path.abspath(os.path.dirname(__file__))


def modify_database_URL(database_URL):
    return database_URL.replace('postgres://', 'postgresql://')


class Config:
    # secret key for forms
    SECRET_KEY = os.getenv("SECRET_KEY")

    # database
    SQLALCHEMY_DATABASE_URI = modify_database_URL(
        os.getenv("DATABASE_URL"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ITEMS_PER_PAGE = 4
