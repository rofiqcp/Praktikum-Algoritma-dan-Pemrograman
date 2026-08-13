import os
from flask import Flask,jsonify

app=Flask(__name__)
app.config["SECRET_KEY"]=os.getenv("APP_SECRET","dev-only-not-for-production")

@app.get("/")
def home(): return "Praktikum Deployment — service aktif"

@app.get("/health")
def health(): return jsonify({"status":"ok","environment":os.getenv("APP_ENV","development")})

if __name__=="__main__":
    port=int(os.getenv("PORT","5000")); app.run(host="0.0.0.0",port=port,debug=os.getenv("FLASK_DEBUG")=="1")
