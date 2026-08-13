import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"python"))
from importlib import import_module
k=import_module("01_kalkulator_modular"); n=import_module("02_sistem_nilai_modular"); b=import_module("04_bug_hunt")

class TestFunctions(unittest.TestCase):
    def test_total(self): self.assertEqual(k.hitung_total(10000,3),30000)
    def test_total_invalid(self):
        with self.assertRaises(ValueError): k.hitung_total(-1,1)
    def test_grade_boundary(self): self.assertEqual(n.grade(75),"C / Lulus")
    def test_grade_invalid(self):
        with self.assertRaises(ValueError): n.grade(101)
    def test_average(self): self.assertEqual(b.rata_rata_benar([80,90,70]),80)

if __name__ == "__main__": unittest.main()
