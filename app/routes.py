#import the app variable defined in init.py
from app import app

from flask import render_template
#non-flask import for route functionality
from .services import getDrinkRecs #need to put .services so it wont be looking for a python module. This is a services file and not a python module.

#this is the base url
@app.route('/')
@app.route('/kcscateringhomepage') #decorator says this is a route of the flask app 'app' with the url endpoint '/marvelhomepage'
def home():
    drinkrecs = getDrinkRecs()
    return render_template('index.html', drinkrecs=drinkrecs)

@app.route('/kcscateringphotos')
def photos():
    return render_template('photos.html')

@app.route('/kcscartingmenu')
def menu():
    return render_template('menu.html')

@app.route('/kcscateringinfo', methods=['GET','POST'])
def info():
    return render_template('info.html')