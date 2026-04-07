from flask import request
from app import app, db
from models import Product, Inventory

@app.route('/api/products', methods=['POST'])
def create_product():
    try:
        data = request.json

        required_fields = ['name', 'sku', 'price']
        for field in required_fields:
            if field not in data:
                return {"error": f"{field} is required"}, 400

        existing = Product.query.filter_by(sku=data['sku']).first()
        if existing:
            return {"error": "SKU already exists"}, 400

        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=float(data['price'])
        )

        db.session.add(product)
        db.session.flush()

        if 'warehouse_id' in data and 'initial_quantity' in data:
            inventory = Inventory(
                product_id=product.id,
                warehouse_id=data['warehouse_id'],
                quantity=data['initial_quantity']
            )
            db.session.add(inventory)

        db.session.commit()
        return {"message": "Product created", "product_id": product.id}, 201

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500