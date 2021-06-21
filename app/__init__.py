from flask import Flask
# from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
# from config import config_options
# from flask_login import LoginManager
# from flask_mail import Mail
# bootstrap = Bootstrap()
# db = SQLAlchemy()
# mail = Mail()
# login_manager = LoginManager()
# login_manager_session_protection = 'strong'
# login_manager.login_view = 'auth.login'


def create_app(app):
    app = Flask(__name__)
    #Create application configurations
    # app.config.from_object(config_options[config_name])
    #Initializing Flask extensions
    # bootstrap = Bootstrap(app)
    # db.init_app(app)
    # mail.init_app(app)
    # login_manager.init_app(app)
    # from . auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/authenticate')
    #Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app