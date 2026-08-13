import sys
import unittest
from importlib import import_module
from pathlib import Path

PYTHON_DIR = Path(__file__).resolve().parents[1] / "python"
sys.path.insert(0, str(PYTHON_DIR))

kalkulator = import_module("01_kalkulator_modular")
nilai = import_module("02_sistem_nilai_modular")
latihan = import_module("04_bug_hunt")


class TestFunctions(unittest.TestCase):
    def test_total_normal(self):
        self.assertEqual(kalkulator.hitung_total(10000, 3), 30000)

    def test_total_zero(self):
        self.assertEqual(kalkulator.hitung_total(0, 3), 0)

    def test_total_invalid_harga(self):
        with self.assertRaises(ValueError):
            kalkulator.hitung_total(-1, 1)

    def test_format_rupiah(self):
        self.assertEqual(kalkulator.format_rupiah(250000), "Rp250,000")

    def test_validasi_boundary(self):
        self.assertTrue(nilai.validasi(0))
        self.assertTrue(nilai.validasi(100))

    def test_grade_boundary_lulus(self):
        self.assertEqual(nilai.grade(75), "C / Lulus")

    def test_grade_a(self):
        self.assertEqual(nilai.grade(90), "A")

    def test_grade_invalid(self):
        with self.assertRaises(ValueError):
            nilai.grade(101)

    def test_average(self):
        self.assertEqual(latihan.rata_rata_benar([80, 90, 70]), 80)

    def test_average_empty(self):
        with self.assertRaises(ValueError):
            latihan.rata_rata_benar([])


if __name__ == "__main__":
    unittest.main()
