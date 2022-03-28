#import blueprints here for our models/api
from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/test')
def test():
    return jsonify({'database': 'whoa this is some cool data'})
