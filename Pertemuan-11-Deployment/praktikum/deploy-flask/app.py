import os
from flask import Flask,jsonify
app=Flask(__name__)
@app.get('/')
def home(): return 'Deployment OK'
@app.get('/health')
def health(): return jsonify({'status':'ok','environment':os.getenv('APP_ENV','development')})
if __name__=='__main__': app.run(host='0.0.0.0',port=int(os.getenv('PORT','5000')))
