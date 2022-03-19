#import the app variable defined in init.py
from app import app

from flask import render_template

#this is the base url
@app.route('/kcscateringhomepage') #decorator says this is a route of the flask app 'app' with the url endpoint '/marvelhomepage'
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')