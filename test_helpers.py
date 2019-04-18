import unittest
from helpers import Vocabulary, EpithetGenerator


class TestHelpers(unittest.TestCase):

    def test_read_json(self):
        self.assertEqual(Vocabulary.read_json("resources/data.json"), Vocabulary.read_json("resources/data.json"))

    def test_read_json_sad(self):
        self.assertEqual(Vocabulary.read_json("resources/data.json"), "json")

    def test_EpithetGenerator_type(self):
        eg = EpithetGenerator()
        result = type(eg.quantity(2))
        self.assertEqual(result, dict)

    def test_EpithetGenerator_type_sad(self):
        eg = EpithetGenerator()
        result = type(eg.quantity(2))
        self.assertEqual(result, int)
