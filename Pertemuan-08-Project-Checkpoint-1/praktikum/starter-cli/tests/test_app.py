import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import tambah_item,cari_item,hapus_item,statistik

class TestApp(unittest.TestCase):
    def test_add_search(self):
        d=[]; tambah_item(d,"A",10); self.assertEqual(cari_item(d,"a")["nilai"],10)
    def test_duplicate(self):
        d=[]; tambah_item(d,"A",1)
        with self.assertRaises(ValueError): tambah_item(d,"A",2)
    def test_delete_not_found(self): self.assertFalse(hapus_item([],"x"))
    def test_stats_empty(self): self.assertEqual(statistik([])["rata"],0)

if __name__ == "__main__": unittest.main()
