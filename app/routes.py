from flask import Blueprint, jsonify, request, render_template
from .crud import create_product, get_product, update_product, delete_product, get_all_products

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/product', methods=['GET', 'POST'])
def product():
    if request.method == 'POST':
        data = request.json
        product = create_product(data['name'], data['quantity'], data['price'])
        return jsonify({'message': 'Product created successfully', 'id': product.id}), 201
    else:
        products = get_all_products()
        return jsonify([{'id': p.id, 'name': p.name, 'quantity': p.quantity, 'price': p.price} for p in products])

@main.route('/product/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def product_detail(id):
    if request.method == 'GET':
        product = get_product(id)
        return jsonify({'name': product.name, 'quantity': product.quantity, 'price': product.price})
    elif request.method == 'PUT':
        data = request.json
        product = update_product(id, data['name'], data['quantity'], data['price'])
        return jsonify({'message': 'Product updated successfully', 'id': product.id})
    elif request.method == 'DELETE':
        delete_product(id)
        return jsonify({'message': 'Product deleted successfully'})