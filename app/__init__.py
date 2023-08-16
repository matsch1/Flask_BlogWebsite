from flask import Flask
from flask_login import LoginManager
from config import Config
from app.extensions import db
from app.blog.authentication import BlogWriterUser

# Flask factory


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'authentication.index'

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blog import bp as blog_bp
    app.register_blueprint(blog_bp, url_prefix='/blog')

    from app.blog.authentication import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/blog/auth')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'
    
    @login_manager.user_loader
    def load_user(user_id):
        user = BlogWriterUser()
        if user_id == user.id:
            return user
        else:
            return None

    return app
