from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 55000.0, "quantity": 10},
    {"id": 2, "name": "Mobile", "price": 15000.0, "quantity": 25},
    {"id": 3, "name": "Headphones", "price": 2000.0, "quantity": 50},
    {"id": 4, "name": "Smartwatch", "price": 5000.0, "quantity": 30},
    {"id": 5, "name": "Keyboard", "price": 700.0, "quantity": 40},
    {"id": 6, "name": "Mouse", "price": 400.0, "quantity": 45},
    {"id": 7, "name": "External Hard Drive", "price": 3500.0, "quantity": 15},
    {"id": 8, "name": "Pen Drive", "price": 500.0, "quantity": 100},
    {"id": 9, "name": "Monitor", "price": 12000.0, "quantity": 12},
    {"id": 10, "name": "Printer", "price": 8000.0, "quantity": 8},
    {"id": 11, "name": "Router", "price": 2200.0, "quantity": 20},
    {"id": 12, "name": "Speakers", "price": 2500.0, "quantity": 25},
    {"id": 13, "name": "Webcam", "price": 1800.0, "quantity": 18},
    {"id": 14, "name": "Projector", "price": 25000.0, "quantity": 5},
    {"id": 15, "name": "Graphic Tablet", "price": 6500.0, "quantity": 7}
]

@app.route('/products', methods=['GET'])
def show_product():
    return jsonify(products)

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    for product in products:
        if product['id'] == int(id):
            return jsonify(product)     
    return jsonify({"error": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.get_json()
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    updated_data = request.get_json()
    for product in products:
        if product['id'] == id:
            product.update(updated_data)
            return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    for product in products:
        if product['id'] == id:
            products.remove(product)
            return jsonify({"message": "Product deleted"}), 200
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)