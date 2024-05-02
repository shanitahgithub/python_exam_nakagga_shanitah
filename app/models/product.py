from flask import Flask
from app.extensions import db





class Product(db.Model):
    __tablename__="products"
    # Attributes of the products and their respective constraints  
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String(50), nullable=False)
    price=db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(20), nullable=False)
    quantity =db.Column(db.String(255), nullable=False)
    
    
# Creating a constructor for the product model
    
    def __init__(self,name,price,description,quantity):
        self.name=name
        self.price= price
        self.description= description
        self.quantity= quantity
        

    def get_name(self):
        return f'{self.name}'

