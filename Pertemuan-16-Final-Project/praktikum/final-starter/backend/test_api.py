import tempfile
from pathlib import Path
import db
import app as module

with tempfile.TemporaryDirectory() as tmp:
    db.DB = Path(tmp) / 'test.db'
    db.init_db()
    module.app.config['TESTING'] = True
    client = module.app.test_client()

    assert client.get('/api/health').status_code == 200
    assert client.get('/api/categories').status_code == 200

    response = client.post('/api/products', json={
        'name': 'Starter Test Product',
        'category_id': 1,
        'price': 1000,
        'stock': 5,
    })
    assert response.status_code == 201, response.get_json()
    product_id = response.get_json()['id']

    assert client.get('/api/products?q=Starter').status_code == 200
    assert client.get(f'/api/products/{product_id}').status_code == 200
    assert client.patch(f'/api/products/{product_id}', json={'stock': 9}).status_code == 200
    assert client.post('/api/products', json={'name': '', 'category_id': 1, 'stock': -1}).status_code == 400
    assert client.delete(f'/api/products/{product_id}').status_code == 204
    assert client.get(f'/api/products/{product_id}').status_code == 404

print('Final starter API smoke test: PASS')
