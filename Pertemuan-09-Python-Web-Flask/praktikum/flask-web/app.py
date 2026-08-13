from flask import Flask,render_template,request,redirect,url_for,flash
app=Flask(__name__); app.config['SECRET_KEY']='dev-only-change-me'
products=[{'id':1,'name':'Keyboard','price':250000,'stock':10},{'id':2,'name':'Mouse','price':125000,'stock':8}]
@app.get('/')
def home(): return render_template('index.html')
@app.get('/products')
def list_products(): return render_template('products.html',products=products)
@app.route('/products/new',methods=['GET','POST'])
def add_product():
    errors={}
    if request.method=='POST':
        name=request.form.get('name','').strip()
        try: price=float(request.form.get('price','')); stock=int(request.form.get('stock',''))
        except ValueError: price=stock=-1; errors['number']='Harga/stok harus angka'
        if not name: errors['name']='Nama wajib'
        if price<0 or stock<0: errors['range']='Tidak boleh negatif'
        if not errors:
            products.append({'id':max(p['id'] for p in products)+1,'name':name,'price':price,'stock':stock})
            flash('Produk tersimpan','success'); return redirect(url_for('list_products'))
    return render_template('form.html',errors=errors)
if __name__=='__main__': app.run(debug=True)
