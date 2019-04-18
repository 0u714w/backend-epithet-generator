#! python3

from flask import Flask, jsonify
from .helpers import Vocabulary, EpithetGenerator
import os

app = Flask(__name__)

path = os.path.abspath("resources/data.json")

@app.route('/')
def generate_epithets():
    d = EpithetGenerator()
    return d.one_random_word()

@app.route('/vocabulary')
def vocabulary():
    v = Vocabulary()
    vocab = v.read_json(path)
    return jsonify(vocab["Column 1"] + vocab["Column 2"] + vocab["Column 3"])