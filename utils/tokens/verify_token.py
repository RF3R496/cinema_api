from jwt import decode
from jwt import exceptions
from decouple import config
from flask import jsonify

def validate_token_user(token,):
    try:
       
        return decode(token,key = config('SECRET_KEY'),algorithms='HS256')
        
    except exceptions.DecodeError:
        return jsonify({'message': 'Invalid Token'}), 401

    except exceptions.ExpiredSignatureError:
        return jsonify({'message' : 'Expired Token '}), 401


def validate_token_admin(token):
    try:
        
        return decode(token,key = config('SECRET_ADMIN_KEY'),algorithms='HS256')

    except exceptions.DecodeError:
        return jsonify({'message': 'Invalid Token'}), 401

    except exceptions.ExpiredSignatureError:
        return jsonify({'message' : 'Expired Token '}), 401