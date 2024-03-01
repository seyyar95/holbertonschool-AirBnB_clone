#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models import storage
from models.state import State


class TestState(unittest.TestCase):

    def test_state(self):
        instance = State()
        instance.name = "Wuhan"
        self.assertIn(instance.name, instance.__dict__)
