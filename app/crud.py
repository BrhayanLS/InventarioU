from .models import Product
from . import db

def create_product(name, quantity, price):
    new_product = Product(name=name, quantity=quantity, price=price)
    db.session.add(new_product)
    db.session.commit()
    return new_product

def get_product(id):
    return Product.query.get_or_404(id)

def get_all_products():
    return Product.query.all()

def update_product(id, name, quantity, price):
    product = Product.query.get_or_404(id)
    product.name = name
    product.quantity = quantity
    product.price = price
    db.session.commit()
    return product

def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()