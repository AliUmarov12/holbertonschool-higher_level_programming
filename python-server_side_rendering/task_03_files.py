from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# -------------------------
# JSON oxuma funksiyası
# -------------------------
def read_json_file(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except Exception as e:
        print("JSON error:", e)
        return []

# -------------------------
# CSV oxuma funksiyası
# -------------------------
def read_csv_file(filename):
    products = []
    try:
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception as e:
        print("CSV error:", e)
    return products

# -------------------------
# SQLite oxuma funksiyası
# -------------------------
def read_sqlite_db(db_file='products.db'):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
        return products
    except Exception as e:
        print("Database error:", e)
        return []

# -------------------------
# Flask route
# -------------------------
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    products_data = []

    if source == "json":
        products_data = read_json_file("products.json")
    elif source == "csv":
        products_data = read_csv_file("products.csv")
    elif source == "sql":
        products_data = read_sqlite_db("products.db")
    else:
        return render_template("product_display.html", error="Wrong source", products=None)

    # ID varsa filter et
    if product_id is not None:
        filtered = [p for p in products_data if p["id"] == product_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found", products=None)
        products_data = filtered

    return render_template("product_display.html", products=products_data, error=None)

@app.route('/')
def home():
    return "<h1>Welcome! Use /products?source=json|csv|sql</h1>"

if __name__ == "__main__":
    app.run(debug=True)
