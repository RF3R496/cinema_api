from werkzeug.security import generate_password_hash

def generate_password(password):
    return generate_password_hash(password,'pbkdf2:sha256',30)
