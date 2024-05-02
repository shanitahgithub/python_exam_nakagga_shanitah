from flask import Blueprint, request, jsonify
from app.models.product import Product
from app.extensions import db


product = Blueprint('product', __name__, url_prefix='/api/v1/product')
# Creating a new product
@product.route('/create', methods=['POST'])
def create_product():
    try:
        # Extracting request data
        name = request.json.get('name')
        price= request.json.get('price')
        description = request.json.get('description')
        quantity= request.json.get('quantity')
        
        # Basic input validation
        if not name:
            return jsonify({"error": 'Product name is required'}), 400

        if not price:
            return jsonify({"error": 'Product price is required'}), 400

        if not description:
            return jsonify({"error": 'Product description is required'}), 400
        
        if Product.query.filter_by(name=name).first():
            return jsonify({"error":'Product already exists'})

        # Creating a new product
        new_product = Product(
            name=name,
            price=price,
            description=description,
            quantity=quantity
        )

        # Adding the new product to the session
        db.session.add(new_product)
        
        # Committing the changes to the database
        db.session.commit()

        # Building a response message
        message = f" {new_product.name}    has been successfully created"
        return jsonify({"message": message,
                     'product':{
                         'product_id':new_product.id,
                         'product_name':new_product.name,
                         'price':new_product.price,
                         'description':new_product.description,
                         'quntity':new_product.quantity} }), 201

    except Exception as e:
        # Rolling back the session in case of an error
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
  
# Retrieving all products in the store
@product.route('/allProducts', methods=["GET"])
def get_all_products():
    try:
        
       

        # Querying all products from the database
        allProducts = Product.query.all()

        # Serializing product data
        serialized_allProducts = []
        for product in allProducts:
            serialized_product= {
                'id': product.id,
                'product_name': product.name,
                'price': product.price,
                'description': product.description,
                
                'quantity': product.quantity,

            }
            serialized_allProducts.append(serialized_product)

        # Returning the serialized product data
        return jsonify({'products': serialized_allProducts}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
   

# Deleting a product from the store
@product.route('/delete/<int:id>', methods=["DELETE"])
def delete_product(id):
    try:
        
        # Retrieving the product to delete
        product= Product.query.filter_by(id=id).first()
        if not product:
            return jsonify({'error': 'Product not found'}), 404

        # Deleting the product
        db.session.delete(product)
        db.session.commit()

        return jsonify({'message': 'Product has been deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
