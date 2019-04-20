#! python3

from flask import Flask, jsonify
from .helpers import Vocabulary, EpithetGenerator
import os
from random import randint

app = Flask(__name__)

path = os.path.abspath("resources/data.json")


@app.route('/')
def generate_epithets():
    e = EpithetGenerator()
    epithet = e.one_random_word()
    return jsonify(epithet)

@app.route('/vocabulary')
def generate_vocabulary():
    v = Vocabulary()
    vocab = v.read_json(path)
    return jsonify(vocab["Column 1"] + vocab["Column 2"] + vocab["Column 3"])

@app.route('/<quantity>')
def generate_epithets_by_quantity(quantity):
    e = EpithetGenerator()
    epithets = e.quantity(quantity)
    return jsonify(epithets)

@app.route('/random')
def generate_random_number_epithets():
    # random = int(randint(1, 101))
    e = EpithetGenerator()
    epithets = e.quantity(randint(1, 101))
    return jsonify(epithets)


