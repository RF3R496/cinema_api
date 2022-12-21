from jwt import encode
#Import the funtion for generate the token duration time 
from ..dates.date_expiration import expiration_time_minutes
from decouple import config

def generate_token_admin(data: dict):
    token = encode(payload={**data, 'exp': expiration_time_minutes(15)},key = config('SECRET_ADMIN_KEY'),algorithm='HS256')
    return token.encode('UTF8')

def generate_token_user(data: dict):
    token = encode(payload={**data, 'exp': expiration_time_minutes(15)},key = config('SECRET_KEY'),algorithm='HS256')
    return token.encode('UTF8')

