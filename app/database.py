from .models import Product
from . import db

def init_db(app):
    with app.app_context():
        db.create_all()