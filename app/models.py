
from flask_sqlalchemy import SQLAlchemy

#CREATE THE INSTANCE OF OUR ORM(OBJECT RELATIONAL MAPPER AKA TRANSLATOR BETWEEN PYTHON AND SQL)
db = SQLAlchemy()

#import login manager and tools and create the instance of our login manager
from flask_login import LoginManager, UserMixin
#create the instance
login = LoginManager()
#neccessary function for our login manager
@login.user_loader
def load_user(user_id):
    return Customer.query.get(user_id)


#initial blueprint setup
from flask import Blueprint, jsonify, request
#import blueprints
# from .auth.routes import auth
from .api.routes import api



# tools for our models
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4
from secrets import token_hex



#IN THE FUTURE NEED TO LOOK AT ADDING FOREIGN KEYS TO LINK THESE CHARTS.BUT FOR NOW THIS PERSON ONLY WANTS TO 
#THE CUSTOMERS TABLE SO THIS IS SOMETHING I WILL WORK ON IN THE FUTURE.
class Customer(db.Model, UserMixin):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(250), nullable=True, unique=True)
    address = db.Column(db.String(250))
    password = db.Column(db.String(250), nullable=False)
    first_name =db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, username, phone, email, address, password, first_name='', last_name=''):
        self.username = username
        self.phone = phone
        self.email = email.lower()
        self.address = address
        self.password = generate_password_hash(password)
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
  


class Inventory(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    product_cost = db.Column(db.Float(2), nullable=False)
    amount_in_inventory = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, product_cost, amount_in_inventory):
        self.name = name
        self.description = description
        self.product_cost = product_cost
        self.amount_in_inventory = amount_in_inventory
        self.id = str(uuid4())

class Products(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    image = db.Column(db.String(250), nullable=True)#not a good idea to store this image in here unless you use no sql.
    price = db.Column(db.Float(2), nullable=False) #ask to be sure
    product_cost = db.Column(db.Float(2), nullable=False)
    order_date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    

    def __init__(self, name, description, price, product_cost):
        self.name = name
        self.description = description
        self.price = price
        self.product_cost = product_cost
        self.id = str(uuid4())
        
        
         


