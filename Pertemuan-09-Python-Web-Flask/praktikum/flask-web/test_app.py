import unittest
import app as module

class FlaskWebTest(unittest.TestCase):
    def setUp(self):
        module.app.config.update(TESTING=True,SECRET_KEY="test"); self.client=module.app.test_client()
    def test_three_pages(self):
        for path in ["/","/about","/products"]: self.assertEqual(self.client.get(path).status_code,200)
    def test_404(self): self.assertEqual(self.client.get("/nope").status_code,404)
    def test_invalid_form(self):
        r=self.client.post("/products/new",data={"name":"","price":"-1","stock":"x"}); self.assertEqual(r.status_code,200); self.assertIn(b"wajib",r.data)
    def test_valid_form(self):
        r=self.client.post("/products/new",data={"name":"Monitor","price":"1000000","stock":"2"},follow_redirects=True); self.assertEqual(r.status_code,200); self.assertIn(b"Monitor",r.data)

if __name__=="__main__": unittest.main()
