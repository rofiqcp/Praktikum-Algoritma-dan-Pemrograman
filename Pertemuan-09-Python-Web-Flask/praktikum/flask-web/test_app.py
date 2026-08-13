import unittest
import app as module


class FlaskWebTest(unittest.TestCase):
    def setUp(self):
        module.app.config.update(TESTING=True)
        module.reset_products()
        self.client = module.app.test_client()

    def test_main_pages_return_200(self):
        for path in ["/", "/about", "/products", "/products/new"]:
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 200)

    def test_product_detail_exists(self):
        response = self.client.get("/products/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Keyboard", response.data)

    def test_unknown_route_returns_404(self):
        response = self.client.get("/route-tidak-ada")
        self.assertEqual(response.status_code, 404)

    def test_invalid_form_shows_field_errors(self):
        response = self.client.post(
            "/products/new",
            data={"name": "", "price": "-1", "stock": "1.5"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Nama wajib diisi", response.data)
        self.assertIn(b"Harga harus", response.data)
        self.assertIn(b"Stok harus", response.data)

    def test_valid_form_is_saved_and_redirected(self):
        response = self.client.post(
            "/products/new",
            data={"name": "Monitor", "price": "1500000", "stock": "2"},
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Monitor", response.data)
        self.assertIn(b"berhasil ditambahkan", response.data)

    def test_stock_zero_is_valid_boundary(self):
        response = self.client.post(
            "/products/new",
            data={"name": "Adaptor", "price": "50000", "stock": "0"},
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Adaptor", response.data)
        self.assertIn(b"Habis", response.data)

    def test_duplicate_name_is_rejected_case_insensitively(self):
        response = self.client.post(
            "/products/new",
            data={"name": "keyboard", "price": "1", "stock": "1"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"sudah ada", response.data)
        self.assertEqual(len(module.products), len(module.INITIAL_PRODUCTS))

    def test_search_is_case_insensitive(self):
        response = self.client.get("/products?q=KEY")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Keyboard", response.data)
        self.assertNotIn(b"Mouse", response.data)

    def test_search_no_result_has_clear_empty_state(self):
        response = self.client.get("/products?q=tidakada")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tidak ada produk", response.data)

    def test_each_test_starts_from_initial_data(self):
        self.assertEqual(len(module.products), len(module.INITIAL_PRODUCTS))


if __name__ == "__main__":
    unittest.main()
