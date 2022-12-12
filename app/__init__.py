from flask import Flask
from config import SQLALCHEMY_DATABASE, SECRET_KEY
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = SECRET_KEY
    

    from .models.models import configure

    db.init_app(app)
    configure(app)
    with app.app_context():

        from .Admin.admin import Admin
        app.register_blueprint(Admin)

    return app
            
        
        

  




   
    
