
from flask_sqlalchemy import SQLAlchemy

#CREATE THE INSTANCE OF OUR ORM(OBJECT RELATIONAL MAPPER AKA TRANSLATOR BETWEEN PYTHON AND SQL)
db = SQLAlchemy()

#initial blueprint setup
from flask import Blueprint, jsonify, request
#import blueprints
# from .auth.routes import auth
from .api.routes import api

#create a link of communication between blueprints and app
#aka register the blueprints
# app.register_blueprint(auth)
# app.register_blueprint(api)


#Login Manager Tools

# create the instance of our login manager


# tools for our models
# tools for our models
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4
from secrets import token_hex



#IN THE FUTURE NEED TO LOOK AT ADDING FOREIGN KEYS TO LINK THESE CHARTS.BUT FOR NOW THIS PERSON ONLY WANTS TO 
#THE CUSTOMERS TABLE SO THIS IS SOMETHING I WILL WORK ON IN THE FUTURE.
class Inventory(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    image = db.Column(db.String(250), nullable=True)
    product_cost = db.Column(db.Float(2), nullable=False)
    amount_in_inventory = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, image, product_cost, amount_in_inventory):
        self.name = name
        self. description = description
        self. image = image
        self.product_cost = product_cost
        self.amount_in_inventory = amount_in_inventory
        self.id = str(uuid4())

class Products(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    image = db.Column(db.String(250), nullable=True)#not a good idea to store this image in here unless you use no sql.
    price = db.Column(db.Float(2), nullable=False) #ask to be sure
    product_cost = db.Column(db.Float(2), nullable=False)
    order_date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    
    
    
    
    def __init__(self, name, description, image, price, product_cost):
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.product_cost = product_cost
        self.id = str(uuid4())
        
        
         


class Customer(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(250), nullable=True, unique=True)
    password = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=True)
    image = db.Column(db.String(250))
    date = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, first_name, last_name, phone, email, password, address, image, date):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.lower()
        self.phone = phone
        self.email = email
        self.password = password
        self.address = address
        self.image = image
        self.id = str(uuid4())
  