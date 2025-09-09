from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import json


app = Flask(__name__)

# Create a connection to the MySQL database
def get_db_connection():
    return mysql.connector.connect(
            host='localhost',
            user='root',
            password='16122003',
            database='ecommercedb'
        )

# load data from JSON file into the database
def load_products_from_json():
    try:
        with open('products.json') as file:
            products = json.load(file)

        connection = get_db_connection()
        cursor = connection.cursor()

        for product in products:
            query = "INSERT INTO products (name, description, price, stock) VALUES (%s, %s, %s, %s)"
            values = (
                product['name'],
                product['description'],
                product['price'],
                product['stock']
            )
            cursor.execute(query, values)

        connection.commit()
        print(f"{cursor.rowcount} products inserted.")
    except Exception as e:
        print("Error loading products:", e)
    finally:
        cursor.close()
        connection.close()

#get all products
@app.route('/products', methods=['GET'])
def get_all_products():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(products), 200

# get a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    cursor.close()
    connection.close()
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404
    
# Add a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO products (id, name, description, price, stock) VALUES (%s, %s, %s, %s, %s)"
        values = (data['id'], data['name'], data['description'], data['price'], data['stock'])
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Product created successfully"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500

# Update a product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "UPDATE products SET name = %s, description = %s, price = %s, stock = %s WHERE id = %s"
        values = (data['name'], data['description'], data['price'], data['stock'], product_id)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        if cursor.rowcount:
            return jsonify({"message": "Product updated"})
        return jsonify({"error": "Product not found"}), 404
    except Error as e:
        return jsonify({"error": str(e)}), 500
    
# delete a product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "DELETE FROM products WHERE id = %s"
        cursor.execute(query, (product_id,))
        connection.commit()
        cursor.close()
        connection.close()
        if cursor.rowcount:
            return jsonify({"message": "Product deleted"}), 200
        return jsonify({"error": "Product not found"}), 404
    except Error as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    load_products_from_json()
    app.run(debug=True)
