from flask import jsonify
from app import app, db
from models import Inventory, Warehouse, Product, Supplier, ProductSupplier

@app.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    alerts = []

    inventories = db.session.query(Inventory).join(Warehouse)\
        .filter(Warehouse.company_id == company_id).all()

    for inv in inventories:
        product = Product.query.get(inv.product_id)

        threshold = 20

        if inv.quantity < threshold:
            daily_sales = 1
            days_left = inv.quantity // daily_sales if daily_sales else None

            supplier = db.session.query(Supplier)\
                .join(ProductSupplier)\
                .filter(ProductSupplier.product_id == product.id).first()

            alerts.append({
                "product_id": product.id,
                "product_name": product.name,
                "sku": product.sku,
                "warehouse_id": inv.warehouse_id,
                "warehouse_name": inv.warehouse.name,
                "current_stock": inv.quantity,
                "threshold": threshold,
                "days_until_stockout": days_left,
                "supplier": {
                    "id": supplier.id if supplier else None,
                    "name": supplier.name if supplier else None,
                    "contact_email": supplier.contact_email if supplier else None
                }
            })

    return jsonify({
        "alerts": alerts,
        "total_alerts": len(alerts)
    })