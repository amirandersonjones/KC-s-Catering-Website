#import ORM
from flask_sqlalchemy import SQLAlchemy

#CREATE THE INSTANCE OF OUR ORM(OBJECT RELATIONAL MAPPER AKA TRANSLATOR BETWEEN PYTHON AND SQL)
db = SQLAlchemy

# tools for our models
from datetime import datetime, timezone
from uuid import uuid4 #the standard normal id a fuction is generated here so we have to string it in our init method


# Kellie Food Products should include the following fields:
# - id (Integer)
# - name (String)
# - description (String)
# - price (Integer)
# - product_cost (String)
# -item_image (String)
#-order_date_created



# class Products(db.Model):
#     id = db.Column(db.String(50), primary_key=True)
#     name = db.Column(db.String(100), unique=True, nullable=False)
#     description = db.Column(db.String(255), nullable=True)
#     image = db.Column(db.String(250), nullable=True)#not a good idea to store this image in here unless you use no sql.
#     price = db.Column(db.Float(2), nullable=False) #ask to be sure
#     product_cost = db.Column(db.Float(2), nullable=False)
#     order_date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

# def __init__(self, dict):
#         """
#         expected dict struture:
#         {
#             'name': <str>,
#             'price': <float(2)> #ask to be sure
#             'product_cost': <float(2)>
#              ###rest of k:v pairs optional
#             'description': <str>,
#             'image': <str>
        
#         }
#         """