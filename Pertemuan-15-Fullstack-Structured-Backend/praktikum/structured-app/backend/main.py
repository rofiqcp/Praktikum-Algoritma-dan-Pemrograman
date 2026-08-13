import os
from flask import Flask,jsonify
from flask_cors import CORS
from db.connection import init_db
from routes.products import bp

def create_app():
    app=Flask(__name__)
    origins=[x.strip() for x in os.getenv('CORS_ORIGINS','http://127.0.0.1:3000,http://localhost:3000').split(',') if x.strip()]
    CORS(app,resources={r"/api/*":{"origins":origins}})
    init_db();app.register_blueprint(bp)
    @app.get('/api/health')
    def health():return jsonify({'status':'ok'})
    return app

app=create_app()
if __name__=='__main__':
    app.run(port=int(os.getenv('API_PORT','5001')),debug=os.getenv('FLASK_DEBUG')=='1')
