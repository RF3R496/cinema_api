from jwt import decode
from jwt import exceptions
from decouple import config
from flask import jsonify

def validate(token, output= False):
    try:
        if output:
            return decode(token,key = config('SECRET_KEY'),algorithms='HS256')
        decode(token,key = config('SECRET_KEY'),algorithms='HS256')
    except exceptions.DecodeError:
        return jsonify({'message': 'Invalid Token'}), 401

    except exceptions.ExpiredSignatureError:
        return jsonify({'message' : 'Expired Token '}), 401
