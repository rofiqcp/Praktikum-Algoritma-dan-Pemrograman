import unittest
from app import app

class DeployAppTest(unittest.TestCase):
    def setUp(self): app.config["TESTING"]=True; self.client=app.test_client()
    def test_home(self): self.assertEqual(self.client.get("/").status_code,200)
    def test_health(self):
        r=self.client.get("/health"); self.assertEqual(r.status_code,200); self.assertEqual(r.get_json()["status"],"ok")

if __name__=="__main__": unittest.main()
