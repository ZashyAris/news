from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .config import config_options
# from .config import DevConfig

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(Config)

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)
    
   
    # Initializing application
    # app = Flask(__name__,instance_relative_config = True)
    
    # # Setting up configuration
    # app.config.from_object(DevConfig)
    # app.config.from_pyfile('config.py')
    # from app import views   

    return app

