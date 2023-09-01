from flask import Flask
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_migrate import Migrate

from config import Config
from website.extensions import db
from website.authentication import BlogWriterUser
from website.extensions import count_lines

# Flask factory


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    # migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'authentication.index'

    pagedown = PageDown(app)

    # Register blueprints here
    from website.main import bp as main_bp
    app.register_blueprint(main_bp)

    from website.blog import bp as blog_bp
    app.register_blueprint(blog_bp, url_prefix='/blog')

    from website.blog.post import bp as post_bp
    app.register_blueprint(post_bp, url_prefix='/blog/post')

    from website.contact import bp as contact_bp
    app.register_blueprint(contact_bp, url_prefix='/contact')

    from website.authentication import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/login')

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

    @app.context_processor
    def inject_number_of_lines():
        number_of_lines = count_lines()
        return dict(number_of_lines=number_of_lines)

    @app.context_processor
    def utility_functions():
        def print_in_console(message):
            print(message)
        return dict(mdebug=print_in_console)

    return app
