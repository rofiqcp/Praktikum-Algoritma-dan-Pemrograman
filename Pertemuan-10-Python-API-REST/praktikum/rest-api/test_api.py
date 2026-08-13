import unittest
import app as module


class ApiTest(unittest.TestCase):
    def setUp(self):
        module.app.config["TESTING"] = True
        module.reset_products()
        self.client = module.app.test_client()

    def test_health_and_collection(self):
        self.assertEqual(self.client.get("/api/health").status_code, 200)
        response = self.client.get("/api/products")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["count"], 2)

    def test_search_states(self):
        self.assertEqual(self.client.get("/api/products?q=KEY").get_json()["count"], 1)
        self.assertEqual(self.client.get("/api/products?q=zzz").get_json()["count"], 0)

    def test_detail_states(self):
        self.assertEqual(self.client.get("/api/products/1").status_code, 200)
        self.assertEqual(self.client.get("/api/products/999").status_code, 404)

    def test_create_valid(self):
        response = self.client.post("/api/products", json={"name":"Monitor","price":10,"stock":2})
        self.assertEqual(response.status_code, 201)

    def test_create_invalid(self):
        self.assertEqual(self.client.post("/api/products", json={"name":"","stock":-1}).status_code, 400)

    def test_duplicate_name(self):
        self.assertEqual(self.client.post("/api/products", json={"name":"keyboard","stock":1}).status_code, 409)

    def test_patch_boundary(self):
        response = self.client.patch("/api/products/1", json={"stock":0})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["stock"], 0)

    def test_patch_validation(self):
        self.assertEqual(self.client.patch("/api/products/1", json={}).status_code, 400)
        self.assertEqual(self.client.patch("/api/products/1", json={"other":1}).status_code, 400)

    def test_delete_and_read_again(self):
        self.assertEqual(self.client.delete("/api/products/1").status_code, 204)
        self.assertEqual(self.client.get("/api/products/1").status_code, 404)

    def test_wrong_method(self):
        self.assertEqual(self.client.put("/api/products/1", json={"stock":1}).status_code, 405)


if __name__ == "__main__":
    unittest.main()
