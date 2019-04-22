import unittest
from backend_epithet_generator.helpers import Vocabulary, EpithetGenerator

data = Vocabulary.read_json("resources/data.json")
epithet = EpithetGenerator.one_random_word(data)
quantity = EpithetGenerator.quantity(data, 5)


class TestHelpers(unittest.TestCase):

    def test_read_json(self):
        assert isinstance(data, dict)
        assert "artless" in data["Column 1"]
        assert len(data.keys()) == 3

    def test_read_json_sad(self):
        assert isinstance(data, int)
        assert len(data.keys()) == 5

    def test_EpithetGenerator_type(self):
        assert len(epithet.split(" ")) == 4
        assert isinstance(epithet, str)
    #
    def test_EpithetGenerator_type_sad(self):
        assert len(epithet.split(" ")) == 3
        assert isinstance(epithet, dict)

    def test_EpithetGenerator_quantity(self):
        assert isinstance(quantity, dict)
        assert len(quantity) == 5
    #
    def test_EpithetGenerator_quantity_sad(self):
        assert isinstance(quantity, list)
        assert len(quantity) == 4