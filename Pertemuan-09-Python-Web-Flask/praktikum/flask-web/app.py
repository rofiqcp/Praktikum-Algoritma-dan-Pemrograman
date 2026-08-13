from flask import Flask,render_template,request,redirect,url_for,flash

app=Flask(__name__); app.config["SECRET_KEY"]="dev-only-change-me"
products=[{"id":1,"name":"Keyboard","price":250000,"stock":10},{"id":2,"name":"Mouse","price":120000,"stock":6}]

@app.get("/")
def home(): return render_template("home.html")

@app.get("/about")
def about(): return render_template("about.html")

@app.get("/products")
def product_list(): return render_template("products.html",products=products)

@app.route("/products/new",methods=["GET","POST"])
def product_new():
    errors={}
    if request.method=="POST":
        name=request.form.get("name","").strip(); price_raw=request.form.get("price",""); stock_raw=request.form.get("stock","")
        if not name: errors["name"]="Nama wajib diisi."
        try:
            price=float(price_raw)
            if price < 0: raise ValueError
        except ValueError: errors["price"]="Harga harus angka >= 0."
        try:
            stock=int(stock_raw)
            if stock < 0: raise ValueError
        except ValueError: errors["stock"]="Stok harus bilangan bulat >= 0."
        if not errors:
            products.append({"id":max((p["id"] for p in products),default=0)+1,"name":name,"price":price,"stock":stock})
            flash("Produk berhasil ditambahkan.","success"); return redirect(url_for("product_list"))
    return render_template("product_form.html",errors=errors)

@app.errorhandler(404)
def not_found(error): return render_template("404.html"),404

if __name__=="__main__": app.run(debug=True)
