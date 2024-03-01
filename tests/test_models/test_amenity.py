#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def  test_amenity(self):
        instance = Amenity()
        instance.name = "What"
