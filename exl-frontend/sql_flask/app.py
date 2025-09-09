from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
            host='localhost',
            user='root',
            password='16122003',
            database='product_task'
        )

# Get all products
@app.route('/products', methods=['GET'])
def get_all_products():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        return jsonify(products), 200
    except Error as e:
        return jsonify({"GET ALL Products - error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
# Get a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()
        if product:
            return jsonify(product), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Error as e:
        return jsonify({"GET Product - error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
# Create a new product
@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'price' not in data or 'quantity' not in data:
            return jsonify({"error": "Invalid input"}), 400
        
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)", (data['name'], data['price'], data['quantity']))
        connection.commit()
        
        return jsonify({"message": "Product created successfully"}), 201
    except Error as e:
        return jsonify({"Create Product - error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
# Update a product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'price' not in data or 'quantity' not in data:
            return jsonify({"error": "Invalid input"}), 400
        
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE products SET name = %s, price = %s, quantity = %s WHERE id = %s", (data['name'], data['price'], data['quantity'], product_id))
        connection.commit()
        
        if cursor.rowcount == 0:
            return jsonify({"error": "Product not found"}), 404
        
        return jsonify({"message": "Product updated successfully"}), 200
    except Error as e:
        return jsonify({"Update Product - error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
# Delete a product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        connection.commit()
        
        if cursor.rowcount == 0:
            return jsonify({"error": "Product not found"}), 404
        
        return jsonify({"message": "Product deleted successfully"}), 200
    except Error as e:
        return jsonify({"Delete Product - error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
if __name__ == '__main__':
    app.run(debug=True)