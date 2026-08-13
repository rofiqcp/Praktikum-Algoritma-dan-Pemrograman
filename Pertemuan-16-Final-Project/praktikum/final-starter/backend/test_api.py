import tempfile
from pathlib import Path
import app as m
t=tempfile.TemporaryDirectory();m.DB=Path(t.name)/'test.db';m.init_db();c=m.app.test_client();assert c.get('/health').status_code==200
r=c.post('/api/products',json={'name':'Keyboard','category_id':1,'stock':5});assert r.status_code==201,r.get_json();i=r.get_json()['id']
assert c.get('/api/products').get_json()['data'][0]['name']=='Keyboard';assert c.patch(f'/api/products/{i}',json={'stock':9}).status_code==200;assert c.delete(f'/api/products/{i}').status_code==204;assert c.post('/api/products',json={'name':'','category_id':1,'stock':-1}).status_code==400
print('Final starter API tests lulus')
