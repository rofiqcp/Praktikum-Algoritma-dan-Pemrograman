import tempfile
import unittest
from pathlib import Path
import app as module
import db

class IntegratedBackendTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        db.DB_PATH = Path(self.tmp.name) / 'test.db'
        db.init_db()
        module.app.config['TESTING'] = True
        self.c = module.app.test_client()

    def tearDown(self):
        self.tmp.cleanup()

    def test_health_and_seed(self):
        self.assertEqual(self.c.get('/api/health').status_code, 200)
        r = self.c.get('/api/products')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.get_json()['data']), 2)

    def test_detail_states(self):
        self.assertEqual(self.c.get('/api/products/1').status_code, 200)
        self.assertEqual(self.c.get('/api/products/999999').status_code, 404)

    def test_create_valid(self):
        r = self.c.post('/api/products', json={'name':'Monitor','price':1000,'stock':0})
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.get_json()['stock'], 0)

    def test_create_validation(self):
        self.assertEqual(self.c.post('/api/products', json={'name':'','stock':-1}).status_code, 400)
        self.assertEqual(self.c.post('/api/products', json=['not-object']).status_code, 400)
        self.assertEqual(self.c.post('/api/products', json={'name':'X','extra':1}).status_code, 400)
        self.assertEqual(self.c.post('/api/products', json={'name':'X','stock':1.2}).status_code, 400)

    def test_duplicate(self):
        self.assertEqual(self.c.post('/api/products', json={'name':'Keyboard'}).status_code, 409)

    def test_patch(self):
        r = self.c.patch('/api/products/1', json={'stock':11})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()['stock'], 11)
        self.assertEqual(self.c.patch('/api/products/1', json={}).status_code, 400)

    def test_remove_resource(self):
        self.assertEqual(self.c.delete('/api/products/1').status_code, 204)
        self.assertEqual(self.c.get('/api/products/1').status_code, 404)
        self.assertEqual(self.c.delete('/api/products/999999').status_code, 404)

if __name__ == '__main__':
    unittest.main()
