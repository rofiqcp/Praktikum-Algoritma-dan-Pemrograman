import unittest,uuid
from main import create_app

class BackendTest(unittest.TestCase):
    def setUp(self): self.c=create_app().test_client()
    def test_health(self): self.assertEqual(self.c.get('/api/health').status_code,200)
    def test_join_list(self):
        r=self.c.get('/api/products'); self.assertEqual(r.status_code,200); self.assertIn('category_name',r.get_json()['data'][0])
    def test_invalid_category(self): self.assertEqual(self.c.post('/api/products',json={'name':'X','category_id':99999,'price':1,'stock':1}).status_code,400)
    def test_create(self):
        name='T-'+uuid.uuid4().hex[:8]; r=self.c.post('/api/products',json={'name':name,'category_id':1,'price':1,'stock':1}); self.assertEqual(r.status_code,201)
    def test_stock_insufficient(self): self.assertEqual(self.c.post('/api/products/1/stock-movements',json={'qty':-999999,'note':'test'}).status_code,409)
    def test_not_found(self): self.assertEqual(self.c.get('/api/products/999999').status_code,404)

if __name__=='__main__':unittest.main()
