import rename_sets
import os
import unittest
import shutil

class TestRenameSetsScript(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        os.makedirs('test_dir')

    def test_file_rename(self):
        test_file_name = 'AetherAerathi[#].xlhq.img'
        expected_file_name = 'AEtherAErathi#.full.img'
        test_dir = 'test_dir'
        os.system('touch ' + test_dir + '/' + test_file_name)
        rename_sets.rename_files(test_dir)
        self.assertTrue(os.path.exists(test_dir + '/' + expected_file_name))
        self.assertFalse(os.path.exists(test_dir + '/' + test_file_name))

    @classmethod
    def tearDownClass(self):
        shutil.rmtree('test_dir/')
