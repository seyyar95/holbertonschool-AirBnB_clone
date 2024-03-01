#!/usr/bin/python3
""" Tests for BaseModel class"""


import unittest
from models.base_model import BaseModel
from models import storage 


class TestBaseModel(unittest.TestCase):
    
    def test_save(self):
        b = BaseModel()
        first_update = b.updated_at
        b.name = "Frank Castle"
        b.my_number = 89
        b.save()
        second_update = b.updated_at
        self.assertIn("BaseModel." + b.id, storage.all())
        self.assertNotEqual(first_update, second_update)

