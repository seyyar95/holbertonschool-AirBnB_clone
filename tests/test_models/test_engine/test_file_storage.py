#!/usr/bin/python3


import unittest
from engine.file_storage.py import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):

    def test_file_path(self):
        self.assertIn(__file_path, FileStorage)

    def test_save(self):
        instance = BaseModel()
        self.storage.new(instance)
        self.assertIn(instance, storage.all())

