import tempfile
import unittest
import uuid
from pathlib import Path
import db.connection as connection
from main import create_app

class BackendTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        connection.DB=Path(self.tmp.name)/'test.db'
        self.c=create_app().test_client()

    def tearDown(self):self.tmp.cleanup()

    def test_health(self):self.assertEqual(self.c.get('/api/health').status_code,200)

    def test_join_list(self):
        r=self.c.get('/api/products');self.assertEqual(r.status_code,200);self.assertIn('category_name',r.get_json()['data'][0])

    def test_filters(self):
        self.assertEqual(self.c.get('/api/products?q=Keyboard').status_code,200)
        self.assertEqual(self.c.get('/api/products?category_id=1').status_code,200)
        self.assertEqual(self.c.get('/api/products?category_id=abc').status_code,400)

    def test_invalid_category(self):
        self.assertEqual(self.c.post('/api/products',json={'name':'X','category_id':99999,'price':1,'stock':1}).status_code,400)

    def test_create(self):
        name='T-'+uuid.uuid4().hex[:8]
        self.assertEqual(self.c.post('/api/products',json={'name':name,'category_id':1,'price':1,'stock':0}).status_code,201)

    def test_invalid_payload_shapes(self):
        self.assertEqual(self.c.post('/api/products',json={'name':'X','category_id':1,'extra':1}).status_code,400)
        self.assertEqual(self.c.post('/api/products',json=['x']).status_code,400)
        self.assertEqual(self.c.post('/api/products',json={'name':'X','category_id':1,'stock':1.5}).status_code,400)

    def test_empty_patch(self):self.assertEqual(self.c.patch('/api/products/1',json={}).status_code,400)

    def test_stock_update(self):
        r=self.c.post('/api/products/1/stock-movements',json={'qty':2,'note':'praktikum'})
        self.assertEqual(r.status_code,201);self.assertEqual(r.get_json()['stock'],12)

    def test_fractional_stock_update(self):
        self.assertEqual(self.c.post('/api/products/1/stock-movements',json={'qty':1.2}).status_code,400)

    def test_not_found(self):self.assertEqual(self.c.get('/api/products/999999').status_code,404)

if __name__=='__main__':unittest.main()
