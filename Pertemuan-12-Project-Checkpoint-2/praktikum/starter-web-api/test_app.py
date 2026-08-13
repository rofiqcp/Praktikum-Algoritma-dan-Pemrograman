import unittest
import app as module

class StarterTest(unittest.TestCase):
    def setUp(self): module.app.config["TESTING"]=True; self.c=module.app.test_client()
    def test_pages(self):
        for p in ["/","/plans","/external"]: self.assertEqual(self.c.get(p).status_code,200)
    def test_health(self): self.assertEqual(self.c.get("/api/health").status_code,200)
    def test_invalid(self): self.assertEqual(self.c.post("/api/plans",json={"title":""}).status_code,400)
    def test_create(self): self.assertEqual(self.c.post("/api/plans",json={"title":"Test plan"}).status_code,201)
    def test_delete_missing(self): self.assertEqual(self.c.delete("/api/plans/999999").status_code,404)

if __name__=="__main__": unittest.main()
