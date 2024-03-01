#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from models import storage
from models.user import User


class TestUser(unittest.TestCase):

    def test_user(self):
        instance = User()
        instance.email = ""
        instance.password = ""
        instance.first_name = ""
        instance.last_name = ""
        self.assertIn("email", instance.__dict__)
        self.assertIn("password", instance.__dict__)
        self.assertIn("first_name", instance.__dict__)
        self.assertIn("last_name", instance.__dict__)
