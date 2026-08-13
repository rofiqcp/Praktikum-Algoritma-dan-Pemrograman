from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)

INITIAL_PRODUCTS = [
    {"id": 1, "name": "Keyboard", "price": 250000.0, "stock": 10},
    {"id": 2, "name": "Mouse", "price": 120000.0, "stock": 6},
    {"id": 3, "name": "Kabel USB", "price": 45000.0, "stock": 0},
]
products = [item.copy() for item in INITIAL_PRODUCTS]


def reset_products():
    """Reset data in-memory agar automated test tidak saling memengaruhi."""
    products.clear()
    products.extend(item.copy() for item in INITIAL_PRODUCTS)


def validate_product(form):
    """Validasi form dan kembalikan data bersih beserta dictionary error."""
    errors = {}
    name = form.get("name", "").strip()
    price_raw = form.get("price", "").strip()
    stock_raw = form.get("stock", "").strip()

    if not name:
        errors["name"] = "Nama wajib diisi."
    elif any(p["name"].lower() == name.lower() for p in products):
        errors["name"] = "Nama produk sudah ada."

    try:
        price = float(price_raw)
        if price < 0:
            raise ValueError
    except (TypeError, ValueError):
        price = None
        errors["price"] = "Harga harus berupa angka >= 0."

    try:
        stock = int(stock_raw)
        if stock < 0:
            raise ValueError
    except (TypeError, ValueError):
        stock = None
        errors["stock"] = "Stok harus bilangan bulat >= 0."

    return {"name": name, "price": price, "stock": stock}, errors


@app.get("/")
def home():
    return render_template(
        "home.html",
        total_products=len(products),
        total_stock=sum(p["stock"] for p in products),
    )


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/products")
def product_list():
    q = request.args.get("q", "").strip()
    saved = request.args.get("saved") == "1"
    filtered = products
    if q:
        needle = q.lower()
        filtered = [p for p in products if needle in p["name"].lower()]
    return render_template("products.html", products=filtered, q=q, saved=saved)


@app.get("/products/<int:product_id>")
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        abort(404)
    return render_template("product_detail.html", product=product)


@app.route("/products/new", methods=["GET", "POST"])
def product_new():
    errors = {}
    values = {"name": "", "price": "", "stock": ""}

    if request.method == "POST":
        values = {
            "name": request.form.get("name", ""),
            "price": request.form.get("price", ""),
            "stock": request.form.get("stock", ""),
        }
        clean, errors = validate_product(request.form)

        if not errors:
            next_id = max((p["id"] for p in products), default=0) + 1
            products.append(
                {
                    "id": next_id,
                    "name": clean["name"],
                    "price": clean["price"],
                    "stock": clean["stock"],
                }
            )
            return redirect(url_for("product_list", saved=1))

    return render_template("product_form.html", errors=errors, values=values)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
