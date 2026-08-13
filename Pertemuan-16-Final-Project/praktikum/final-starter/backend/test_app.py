import tempfile
import unittest
from pathlib import Path
import app as module
import db

class FinalApiTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        db.DB=Path(self.tmp.name)/'test.db'
        db.init_db()
        module.app.config['TESTING']=True
        self.c=module.app.test_client()

    def tearDown(self):self.tmp.cleanup()

    def test_health(self):self.assertEqual(self.c.get('/api/health').status_code,200)
    def test_categories(self):self.assertEqual(self.c.get('/api/categories').status_code,200)

    def test_join(self):
        r=self.c.get('/api/products');self.assertEqual(r.status_code,200);self.assertIn('category_name',r.get_json()['data'][0])

    def test_search(self):
        r=self.c.get('/api/products?q=Keyboard');self.assertEqual(r.status_code,200);self.assertEqual(len(r.get_json()['data']),1)

    def test_category_filter(self):self.assertEqual(self.c.get('/api/products?category_id=1').status_code,200)
    def test_invalid_filter(self):self.assertEqual(self.c.get('/api/products?category_id=abc').status_code,400)
    def test_not_found(self):self.assertEqual(self.c.get('/api/products/999999').status_code,404)

    def test_create_boundary(self):
        r=self.c.post('/api/products',json={'name':'Webcam','category_id':1,'price':1,'stock':0});self.assertEqual(r.status_code,201);self.assertEqual(r.get_json()['stock'],0)

    def test_invalid_values(self):self.assertEqual(self.c.post('/api/products',json={'name':'','category_id':1,'price':-1,'stock':-1}).status_code,400)
    def test_non_object(self):self.assertEqual(self.c.post('/api/products',json=['x']).status_code,400)
    def test_unknown_field(self):self.assertEqual(self.c.post('/api/products',json={'name':'X','category_id':1,'extra':1}).status_code,400)
    def test_fractional_stock(self):self.assertEqual(self.c.post('/api/products',json={'name':'X','category_id':1,'stock':1.5}).status_code,400)
    def test_invalid_category(self):self.assertEqual(self.c.post('/api/products',json={'name':'X','category_id':99999,'price':1,'stock':1}).status_code,400)
    def test_duplicate(self):self.assertEqual(self.c.post('/api/products',json={'name':'Keyboard','category_id':1,'price':1,'stock':1}).status_code,409)

    def test_patch(self):
        r=self.c.patch('/api/products/1',json={'stock':12});self.assertEqual(r.status_code,200);self.assertEqual(r.get_json()['stock'],12)

    def test_empty_patch(self):self.assertEqual(self.c.patch('/api/products/1',json={}).status_code,400)
    def test_patch_invalid(self):self.assertEqual(self.c.patch('/api/products/1',json={'stock':-1}).status_code,400)

    def test_remove_existing(self):
        self.assertEqual(self.c.delete('/api/products/1').status_code,204);self.assertEqual(self.c.get('/api/products/1').status_code,404)

    def test_remove_missing(self):self.assertEqual(self.c.delete('/api/products/999999').status_code,404)

    def test_empty_result(self):
        r=self.c.get('/api/products?q=not-present');self.assertEqual(r.status_code,200);self.assertEqual(r.get_json()['data'],[])

if __name__=='__main__':unittest.main()
