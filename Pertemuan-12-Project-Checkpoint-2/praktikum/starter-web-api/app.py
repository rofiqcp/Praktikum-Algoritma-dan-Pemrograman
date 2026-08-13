from flask import Flask,jsonify,render_template
app=Flask(__name__); DATA=[{'id':1,'name':'Sensor A','status':'online'},{'id':2,'name':'Sensor B','status':'offline'}]
@app.get('/')
def home(): return render_template('index.html',items=DATA)
@app.get('/api/items')
def items(): return jsonify({'data':DATA})
@app.get('/api/mock-external')
def mock(): return jsonify({'source':'mock','temperature':29,'unit':'C'})
if __name__=='__main__': app.run(debug=True)
