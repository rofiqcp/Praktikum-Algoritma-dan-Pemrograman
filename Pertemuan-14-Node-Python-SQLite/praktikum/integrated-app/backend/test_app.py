import unittest
import app as module

class IntegratedBackendTest(unittest.TestCase):
    def setUp(self): module.app.config["TESTING"]=True; self.c=module.app.test_client()
    def test_health(self): self.assertEqual(self.c.get('/api/health').status_code,200)
    def test_list(self): self.assertEqual(self.c.get('/api/products').status_code,200)
    def test_invalid(self): self.assertEqual(self.c.post('/api/products',json={'name':'','stock':-1}).status_code,400)
    def test_not_found(self): self.assertEqual(self.c.get('/api/products/999999').status_code,404)

if __name__=='__main__': unittest.main()
