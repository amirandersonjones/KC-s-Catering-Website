#imports at the top of any necessary modules/files/classes/packages/functions
from flask import Flask
#instantiating our Flask Object
# tell the computer this is a flask app

#from our cofig file import the Config class that we created
#from our cofig file import the Config class that we created
from config import Config

app = Flask(__name__)

#go to config.py to tell this app how it should be configured
app.config.from_object(Config)
# aka configure our flas app from the Config object we just wrote

#telling the app the routes.py file is relevant or contains info
from . import routes #from the app folder that we are currently in import the routes

#imports for database stuff
from . models import db
from flask_migrate import Migrate
#setup our ORM and Migrate connections
db.init_app(app)
migrate = Migrate(app, db)
from .import models #tell flask about the existence of any models import from the app folder
