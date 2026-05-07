import unittest
from src.utils import greet

class TestUtils(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")