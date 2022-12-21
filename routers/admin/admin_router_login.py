from flask import Blueprint
from flask import jsonify, request
from utils.password.check_password import check_password
from utils.tokens.create_token import generate_token_admin

#from models.admin.entities.admin_user import AdminUser

from models.admin.admin_login_model import AdminUserModel

admin_route_login = Blueprint('admin_routes', __name__ )

@admin_route_login.route('/', methods=['POST'])
def login():
    try:
        user = request.json['username']
        password = request.json['password']
        admin_user = AdminUserModel.get_for_login(user)
        valid_password = False
        if admin_user == None:
           return jsonify({'message':'Invalid user'}),404
        else :
            valid_password = check_password(admin_user['password'], password)

        if valid_password:
            token = generate_token_admin({
                'id':admin_user['id'],
                'user':admin_user['user'],
            })
        else :
            return jsonify({'message':'here'}),500
        return token
        return jsonify(admin_user)
    except Exception as ex:
        return jsonify({'message':'something was wrong'}), 500
