import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import tambah_item,cari_item,hapus_item,statistik

class TestApp(unittest.TestCase):
    def test_add_search(self):
        d=[]; tambah_item(d,"A",10); self.assertEqual(cari_item(d,"a")["nilai"],10)
    def test_empty_name(self):
        with self.assertRaises(ValueError): tambah_item([]," ",1)
    def test_negative(self):
        with self.assertRaises(ValueError): tambah_item([],"A",-1)
    def test_duplicate(self):
        d=[]; tambah_item(d,"A",1)
        with self.assertRaises(ValueError): tambah_item(d,"a",2)
    def test_delete_existing(self):
        d=[]; tambah_item(d,"A",1); self.assertTrue(hapus_item(d,"A"))
    def test_delete_not_found(self): self.assertFalse(hapus_item([],"x"))
    def test_stats(self):
        d=[]; tambah_item(d,"A",10); tambah_item(d,"B",20); self.assertEqual(statistik(d)["rata"],15)
    def test_stats_empty(self): self.assertEqual(statistik([])["rata"],0)

if __name__ == "__main__": unittest.main()
