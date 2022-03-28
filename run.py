#initial setup of the models to test in the shell

from app import app
from app.models import db, Customer, Products, Inventory
#this allows me to create and update data without having to create routes first/this is for testing
@app.shell_context_processor
def shell_context():
    return {'db': db, 'Customer': Customer, 'Products': Products, 'Inventory': Inventory} #returns a dictionary




