import unittest
import app as module


class StarterTest(unittest.TestCase):
    def setUp(self):
        module.app.config["TESTING"] = True
        module.reset_plans()
        self.client = module.app.test_client()

    def test_pages(self):
        for path in ["/", "/plans", "/external"]:
            self.assertEqual(self.client.get(path).status_code, 200)

    def test_external_page_states(self):
        for mode in ["success", "empty", "timeout", "error"]:
            response = self.client.get("/external?mode=" + mode)
            self.assertEqual(response.status_code, 200)
            self.assertIn(mode.encode(), response.data)

    def test_health(self):
        self.assertEqual(self.client.get("/api/health").status_code, 200)

    def test_list(self):
        response = self.client.get("/api/plans")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["count"], 1)

    def test_detail(self):
        self.assertEqual(self.client.get("/api/plans/1").status_code, 200)
        self.assertEqual(self.client.get("/api/plans/999").status_code, 404)

    def test_create_valid(self):
        self.assertEqual(self.client.post("/api/plans", json={"title": "Test plan"}).status_code, 201)

    def test_create_invalid(self):
        self.assertEqual(self.client.post("/api/plans", json={"title": ""}).status_code, 400)

    def test_patch_valid(self):
        response = self.client.patch("/api/plans/1", json={"status": "done"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "done")

    def test_patch_invalid(self):
        self.assertEqual(self.client.patch("/api/plans/1", json={"status": "unknown"}).status_code, 400)

    def test_delete_missing(self):
        self.assertEqual(self.client.delete("/api/plans/999").status_code, 404)

    def test_external_preview_success(self):
        self.assertEqual(self.client.get("/api/external-preview?mode=success").status_code, 200)

    def test_external_preview_empty(self):
        self.assertEqual(self.client.get("/api/external-preview?mode=empty").status_code, 200)

    def test_external_preview_failure_states(self):
        self.assertEqual(self.client.get("/api/external-preview?mode=timeout").status_code, 503)
        self.assertEqual(self.client.get("/api/external-preview?mode=error").status_code, 503)


if __name__ == "__main__":
    unittest.main()
