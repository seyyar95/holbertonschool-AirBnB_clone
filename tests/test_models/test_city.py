#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
from models.city import City


class TestCity(unittest.TestCase):

    def test_city(self):
        instance = City()
        instance.state_id = "16" 
        instance.name = "Albuquerque"
        self.assertEqual(instance.name, "Albuquerque")
        self.assertEqual(instance.state_id, "16"

