from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)

@app.route('/products', methods=['GET', 'POST'])
# Read products from CSV file
def read_products_from_csv():
    products = []
    try:
        with open('products.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                products.append(row)
    except FileNotFoundError:
        print("CSV file not found.")
    # print("Products loaded from CSV:", products)

    #return the products in the form of a table
    return render_template('show_products.html', products=products)

def load_all_products():
    products = read_products_from_csv()
    return products

def save_product_to_json(product):
    with open('products.json', mode='w') as file:
        json.dump(product, file, indent=4)
    
@app.route('/', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        products = load_all_products()
        new_product = {
            'product_id': request.form['product_id'],
            'product_name': request.form['product_name'],
            'category': request.form['category'],
            'price': request.form['price']
        }
        print("New product added:", new_product)
        products.append(new_product)
        save_product_to_json(products)

        with open('products.csv', mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                new_product["product_id"],
                new_product["product_name"],
                new_product["category"],
                new_product["price"]
            ])  
    return render_template('add_products.html')

if __name__ == '__main__':
    app.run(debug=True)