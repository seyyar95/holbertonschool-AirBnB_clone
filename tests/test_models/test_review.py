#!/user/bin/python3

import unittest
from models.base_model import BaseModel
from models import storage
from models.review import Review


class TestReview(unittest.TestCase):
    def test_review(self):
        instance = Review()
        instance.place_id = "123"
        instance.user_id = "23455"
        instance.text = "Text"
        self.assertEqual(instance.place_id, "123")
        self.assertEqual(instance.text, "Text")
        self.assertEqual(instance.user_id, "23455")
