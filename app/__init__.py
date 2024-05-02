from flask import Flask,jsonify
from app.extensions import db,migrate
from app.controllers.products_controller import product


#application factory function
def create_app():
    
    #app instance
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app,db)
    
    
    from app.models.product import Product



    @app.route("/")
    def home():
        return "Python Exam"
    
  
    app.register_blueprint(product, url_prefix='/api/v1/product')
    

    return app

