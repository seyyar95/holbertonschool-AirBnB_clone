#!/usr/bin/python3


import unittest
from engine.file_storage.py import FileStorage


class TestFileStorage(unittest.TestCase):

    def test_file_path(self):
        
        self.assertIn(__file_path, FileStorage)

