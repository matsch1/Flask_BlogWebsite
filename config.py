from dotenv import load_dotenv
import os

load_dotenv()
base_directory = os.path.abspath(os.path.dirname(__file__))


class Config:
    # secret key for forms
    SECRET_KEY = os.getenv("SECRET_KEY")

    # database
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_directory, 'app.db')
    SQLALCHEMY_DATABASE_URI = "postgres://zofdxfqdfwbhsf:1b936e5e3d0e5630b0b1b5174981e6952dd2862d524c22f477cf6a5bd5a61730@ec2-34-247-94-62.eu-west-1.compute.amazonaws.com:5432/dasoemou698coq"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
