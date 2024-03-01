#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
from models.place import Place


class TestPlace(unittest.TestCase):

    def test_place(self):
        instance = Place()
        instance.name = "Chinar Plaza"
        instance.city_id = 16
        instance.user_id = 23232
        instance.description = "Something meaningful"
        instance.number_rooms = 0
        instance.number_bathrooms = 0
        instance.max_guest = 0
        instance.price_by_night = 0
        instance.latitude = 0.0
        instance.longitude = 0.0
        instance.amenity_ids = []
        self.assertIn(instance.name, instance.__dict__)
