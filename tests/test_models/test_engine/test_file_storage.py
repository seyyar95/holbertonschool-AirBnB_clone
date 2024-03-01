#!/usr/bin/python3


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):

    def test_save(self):
        instance = BaseModel()
        storage.new(instance)
        self.assertIn(instance, storage.all())

