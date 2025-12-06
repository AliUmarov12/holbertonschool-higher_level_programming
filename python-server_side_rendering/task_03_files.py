from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# --- JSON oxuma funksiyası ---
def read_json_file(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except Exception as e:
        return []

# --- CSV oxuma funksiyası ---
def read_csv_file(filename):
    products = []
    try:
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # CSV-də id və price string olaraq gəlir, onları uyğun tiplərə çeviririk
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception as e:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    products_data = []

    # Mənbəyə görə faylı oxu
    if source == "json":
        products_data = read_json_file("products.json")
    elif source == "csv":
        products_data = read_csv_file("products.csv")
    else:
        return render_template("product_display.html", error="Wrong source", products=None)

    # ID varsa filtrlə
    if product_id is not None:
        filtered = [p for p in products_data if p["id"] == product_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found", products=None)
        products_data = filtered

    return render_template("product_display.html", products=products_data, error=None)

if __name__ == "__main__":
    app.run(debug=True)
