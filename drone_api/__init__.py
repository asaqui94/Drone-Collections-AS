from flask import Flask

#TODO: Import Config Object for Flask Project
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Import for Flask Login
from flask_login import LoginManager

#Import for AuthLib integrations
from authlib.integrations.flask_client import OAuth

#Import for Flask- Marshmallow
from flask_marshmallow import  Marshmallow

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'signin' #Specifiy what page to load for NON-Auth users

oauth = OAuth(app)

ma = Marshmallow(app)

from drone_api import routes, models