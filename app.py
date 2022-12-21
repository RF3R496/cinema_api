from flask import Flask
from config import config
#Routes
from routers.admin import admin_router_login

app = Flask(__name__)


def page_not_found(error):
    return '<h1>Page not Found</h1>', 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    #Blueprint 
    app.register_blueprint(admin_router_login.admin_route, url_prefix='/api/admin')
    app.register_error_handler(404, page_not_found)
    app.run()