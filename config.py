#set up and organize the applicationns general config, secret variables, 
# database infor, api keys, file structure,etc
import os


#base directory of the application-help the computer figure out the 
# file system and where to find pieces of the project.allows us to write relative files when needed-css, images, etc


basedir = os.path.abspath(os.path.dirname(__name__))

#config variables setup
class Config:
    """set configuration variables for our entire flask app
    """
#need 3 things variables have to have these names
FLASK_APP = os.environ.get('FLASK_APP')   #TELL THE APP WHAT ITS NAMED
FLASK_ENV = os.environ.get('FLASK_ENV')  #IS THIS APP UNDER DEVELOPMENT, PUBLIC ETC. WILL SKIP SOME SECURITY STEPS IF STILL UNDER DEVELOPMENT AND WILL ACTIVATE MORE DEBUGGER INFO
SECRET_KEY = os.environ.get('SECRET_KEY') #passes the secret key to make sure that it is not being accessed by malicious activities.STORED IN .ENV FILE