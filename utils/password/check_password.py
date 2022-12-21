from werkzeug.security import check_password_hash

def check_password(hash, password):
    hash = hash.replace(' ', '')
    return  check_password_hash(hash, password)
   