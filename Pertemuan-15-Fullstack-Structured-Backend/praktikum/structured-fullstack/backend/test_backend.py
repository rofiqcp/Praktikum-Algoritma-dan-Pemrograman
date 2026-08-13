import tempfile
from pathlib import Path
import db,repository
from app import app
tmp=tempfile.TemporaryDirectory();db.DB_PATH=Path(tmp.name)/'test.db';repository.connect=db.connect;db.init_db();c=app.test_client()
r=c.post('/api/products',json={'name':'Keyboard','category_id':1,'price':250000,'stock':10});assert r.status_code==201,r.get_json()
assert len(c.get('/api/products').get_json()['data'])==1
assert c.post('/api/products',json={'name':'','category_id':999,'price':-1,'stock':-1}).status_code==400
print('Structured backend tests lulus')
