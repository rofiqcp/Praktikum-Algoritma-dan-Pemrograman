from app import app
c=app.test_client(); assert c.get('/api/products').status_code==200
r=c.post('/api/products',json={'name':'Monitor','stock':3}); assert r.status_code==201; i=r.get_json()['id']
assert c.patch(f'/api/products/{i}',json={'stock':5}).status_code==200
assert c.delete(f'/api/products/{i}').status_code==204
assert c.post('/api/products',json={'name':'','stock':-1}).status_code==400
print('API tests lulus')
