import sys
import unittest
from importlib import import_module
from pathlib import Path

PYTHON_DIR = Path(__file__).resolve().parents[1] / "python"
sys.path.insert(0, str(PYTHON_DIR))

statistik_mod = import_module("01_statistik_nilai")
search_mod = import_module("06_pencarian_produk")


class TestDataPertemuan05(unittest.TestCase):
    def test_statistik_normal(self):
        hasil = statistik_mod.statistik([80, 75, 90])
        self.assertEqual(hasil["jumlah"], 3)
        self.assertEqual(hasil["min"], 75)
        self.assertEqual(hasil["max"], 90)
        self.assertEqual(hasil["rata"], 245 / 3)
        self.assertEqual(hasil["lulus"], 3)

    def test_statistik_satu_data(self):
        hasil = statistik_mod.statistik([100])
        self.assertEqual(hasil["min"], 100)
        self.assertEqual(hasil["max"], 100)
        self.assertEqual(hasil["rata"], 100)

    def test_statistik_kosong(self):
        self.assertIsNone(statistik_mod.statistik([]))

    def test_cari_produk_case_insensitive(self):
        hasil = search_mod.cari_produk(search_mod.PRODUK, " keyboard ")
        self.assertIsNotNone(hasil)
        self.assertEqual(hasil["nama"], "Keyboard")

    def test_cari_produk_tidak_ada(self):
        self.assertIsNone(search_mod.cari_produk(search_mod.PRODUK, "Printer"))


if __name__ == "__main__":
    unittest.main()
