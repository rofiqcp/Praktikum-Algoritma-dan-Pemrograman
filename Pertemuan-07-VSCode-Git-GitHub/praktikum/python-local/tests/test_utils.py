import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from utils import hitung_diskon,hitung_bayar

class TestUtils(unittest.TestCase):
    def test_nonmember(self): self.assertEqual(hitung_diskon(200000,False),0)
    def test_member_boundary(self): self.assertEqual(hitung_diskon(100000,True),10000)
    def test_member_below(self): self.assertEqual(hitung_diskon(99999,True),0)
    def test_invalid(self):
        with self.assertRaises(ValueError): hitung_bayar(-1,True)

if __name__ == "__main__": unittest.main()
