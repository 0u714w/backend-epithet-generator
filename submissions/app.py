#! python3

from flask import Flask, jsonify
from .helpers import Vocabulary, EpithetGenerator
import os

app = Flask(__name__)
path = os.path.abspath("resources/data.json")

@app.route('/')
def generate_epithets():
    d = EpithetGenerator()
    epithet = d.one_random_word()
    return jsonify(epithet)

# @app.route('/vocabulary')
# def generate_vocabulary():
#     v = Vocabulary()
#     vocab = v.read_json(path)
#     return jsonify(vocab["Column 1"] + vocab["Column 2"] + vocab["Column 3"])

# @app.route('/<quantity>')
# def generate_epithets_by_quantity(quantity):
#     e = EpithetGenerator()
#     epithets = e.quantity(quantity)
#     return jsonify(epithets)

