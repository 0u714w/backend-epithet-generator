import json
import os
import random


path = os.path.abspath("resources/data.json")


class Vocabulary:

    @staticmethod
    def read_json(path, mode='r'):
        with open(path, mode=mode) as handle:
            return json.load(handle)


class EpithetGenerator:

    def __init__(self):
        self.data = Vocabulary.read_json(path)

    def one_random_word(self):
        word_1 = random.choice(self.data["Column 1"])
        word_2 = random.choice(self.data["Column 2"])
        word_3 = random.choice(self.data["Column 3"])
        return "{}, {}, {}".format(word_1, word_2, word_3)

    def quantity(self, quantity):
        epithets = {}
        for i in range((int(quantity))):
            word_1 = random.choice(self.data["Column 1"])
            word_2 = random.choice(self.data["Column 2"])
            word_3 = random.choice(self.data["Column 3"])
            epithets[i + 1] = ("{}, {}, {}".format(word_1, word_2, word_3))
        return epithets



