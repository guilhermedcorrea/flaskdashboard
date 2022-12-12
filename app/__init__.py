from flask import Flask


def create_app():
    app = Flask(__name__)

    from .Admin.admin import Admin
    app.register_blueprint(Admin)
    return app
    
