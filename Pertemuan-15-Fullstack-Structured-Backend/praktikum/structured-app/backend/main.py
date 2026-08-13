from flask import Flask,jsonify
from flask_cors import CORS
from db.connection import init_db
from routes.products import bp

def create_app():
    app=Flask(__name__); CORS(app,resources={r"/api/*":{"origins":["http://127.0.0.1:3000","http://localhost:3000"]}}); init_db(); app.register_blueprint(bp)
    @app.get('/api/health')
    def health():return jsonify({'status':'ok'})
    return app

app=create_app()
if __name__=='__main__':app.run(port=5001,debug=True)
