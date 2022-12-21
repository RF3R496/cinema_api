from flask import Blueprint, request, jsonify
from decouple import config
from utils.tokens.verify_token import validate_token_admin

admin_route_movie = Blueprint('admin_route_movie', __name__)

information = None
@admin_route_movie.before_request
def valida_token_middleware():
    try:
        token = request.headers['Authorization']

        if token == '': 
            return jsonify({'message': 'Access denied'})
        data = validate_token_admin(token)
        global information 
        information = data
    except Exception as ex:
        raise ex

@admin_route_movie.route('/', methods=['GET'])
def get_movies():
    return jsonify({'msg': information})