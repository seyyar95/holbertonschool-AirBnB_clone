#!/usr/bin/python3
import unittest
from models import storage
from models.state import State


class TestState(unittest.TestCase):

    def test_state(self):
        instance = State()
        instance.name = "Wuhan"
        self.assertEqual(instance.name, "Wuhan")
