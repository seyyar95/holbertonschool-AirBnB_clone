#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from models import storage
from models.user import User


class TestUser(unittest.TestCase):

    def test_user(self):
        instance = User()
        instance.email = "example@gmail.com"
        instance.password = ""
        instance.first_name = ""
        instance.last_name = ""
        self.assertIn(instance.email, "example@gmail.com")
        self.assertIn(instance.password, "")
        self.assertIn(instance.first_name, "")
        self.assertIn(instance.last_name, "")
