import unittest,uuid
import app as module

class FinalApiTest(unittest.TestCase):
    def setUp(self):module.app.config['TESTING']=True;self.c=module.app.test_client()
    def test_health(self):self.assertEqual(self.c.get('/api/health').status_code,200)
    def test_categories(self):self.assertEqual(self.c.get('/api/categories').status_code,200)
    def test_join(self):
        r=self.c.get('/api/products');self.assertEqual(r.status_code,200);self.assertIn('category_name',r.get_json()['data'][0])
    def test_not_found(self):self.assertEqual(self.c.get('/api/products/999999').status_code,404)
    def test_invalid(self):self.assertEqual(self.c.post('/api/products',json={'name':'','category_id':1,'price':-1,'stock':-1}).status_code,400)
    def test_invalid_category(self):self.assertEqual(self.c.post('/api/products',json={'name':'X','category_id':99999,'price':1,'stock':1}).status_code,400)
    def test_create(self):
        n='P-'+uuid.uuid4().hex[:8];self.assertEqual(self.c.post('/api/products',json={'name':n,'category_id':1,'price':1,'stock':0}).status_code,201)
    def test_patch_invalid(self):self.assertEqual(self.c.patch('/api/products/1',json={'stock':-1}).status_code,400)
    def test_delete_missing(self):self.assertEqual(self.c.delete('/api/products/999999').status_code,404)

if __name__=='__main__':unittest.main()
