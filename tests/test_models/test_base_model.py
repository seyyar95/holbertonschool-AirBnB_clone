#!/usr/bin/python3
""" Tests for BaseModel class"""


import unittest
from models.base_model import BaseModel
from models import storage 


class TestBaseModel(unittest.TestCase):
    
    def test_save(self):
        b = BaseModel()
        b.name = "Frank Castle"
        b.my_number = 89
        b.save()
        self.assertIn("BaseModel." + b.id, storage.all()) 


