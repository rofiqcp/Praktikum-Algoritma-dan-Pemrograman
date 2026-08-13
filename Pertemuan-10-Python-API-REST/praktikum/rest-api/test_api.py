import unittest
import app as module

class ApiTest(unittest.TestCase):
    def setUp(self):
        module.app.config["TESTING"]=True; self.client=module.app.test_client()
    def test_health(self): self.assertEqual(self.client.get("/api/health").status_code,200)
    def test_list(self): self.assertEqual(self.client.get("/api/products").status_code,200)
    def test_create_validation(self): self.assertEqual(self.client.post("/api/products",json={"name":"","stock":-1}).status_code,400)
    def test_create(self):
        r=self.client.post("/api/products",json={"name":"TestUniqueProduct","price":1,"stock":0}); self.assertIn(r.status_code,(201,409))
    def test_not_found(self): self.assertEqual(self.client.get("/api/products/999999").status_code,404)
    def test_patch(self): self.assertEqual(self.client.patch("/api/products/1",json={"stock":5}).status_code,200)
    def test_delete_missing(self): self.assertEqual(self.client.delete("/api/products/999999").status_code,404)

if __name__=="__main__": unittest.main()
