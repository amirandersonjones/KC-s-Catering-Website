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

#imports for database stuff + login manager
from .models import db, login
from flask_migrate import Migrate

#set up login manager
login.init_app(app)
login.login_view = 'auth.signin'
login.login_message = 'Please sign in to see this page.'
login.login_message_category = 'danger'

# set up our ORM and Migrate connections
db.init_app(app)
migrate = Migrate(app, db)

#tell flask about the existence of any models import from the app folder
from . import routes
from . import models 
 
#blueprint imports
from .auth.routes import auth
from .api.routes import api
from .blog.routes import blog

#create link of communication between blueprints and app
app.register_blueprint(auth)
app.register_blueprint(api)
app.register_blueprint(blog)