import os
basedir = os.path.abspath(os.path.dirname(__file__)) #creates a basedirectory for environemnt

class Config(object):
    """Base configuration."""

    APP_NAME = 'Flask App'
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Ensure you set a secret key, this is important!')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass 
   
class ProductionConfig(object):
   """Production configuration."""

   SQLALCHEMY_DATABASE_URI = os.environ.get(
      'DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'database.sqlite3'))
   WTF_CSRF_ENABLED = True