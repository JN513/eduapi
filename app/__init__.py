from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_message = "Você deve fazer login para acessar esta página"
bootstrap = Bootstrap()
ma = Marshmallow()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    login.init_app(app)
    bootstrap.init_app(app)
    ma.init_app(app)

    from app.admin import admin as admin_blueprint

    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    from app.api import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api")

    from app.auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from app import views, models

    return app
