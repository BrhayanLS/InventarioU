from flask import Blueprint, jsonify, request, render_template, session, redirect, url_for
from werkzeug.security import check_password_hash
from .crud import create_product, get_product, update_product, delete_product, get_all_products, create_user, get_user_by_username

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if 'user_id' not in session:  # Verifica si el usuario está autenticado
        return redirect(url_for('main.login'))  # Redirige a la página de inicio de sesión
    return render_template('index.html')  # Muestra la página de inicio si está autenticado


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
    
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        user = get_user_by_username(data['username'])
        if user and user.check_password(data['password']):
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        return 'Invalid username or password', 401
    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        user = create_user(data['username'], data['password'])
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Elimina el ID del usuario de la sesión
    return redirect(url_for('main.login'))  # Redirige a la página de inicio de sesión
