import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.config import Config
from werkzeug.exceptions import HTTPException



# Application factory
# Blueprint registration


def create_app(config_class=Config):
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(config_class)
    db.app = app

    app.app_context().push()
    db.init_app(app)


   # from bettercrative.users.routes import users
   
   # Set up extensions.
    db.init_app(app)

    #Register blueprints
   # app.register_blueprint(users)
    
    # Error handlers.
   # @app.errorhandler(HTTPException)
    #def handle_http_error(exc):
    #    return render_template('error.html', error=exc), exc.code


    return app


db = SQLAlchemy()

