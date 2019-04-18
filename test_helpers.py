import unittest
from helpers import Vocabulary

json = Vocabulary.read_json("resources/data.json")

class TestHelpers(unittest.TestCase):

    def test_read_json(self):
        self.assertEqual(Vocabulary.read_json("resources/data.json"), json)
