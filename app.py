#! python3

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def generate_epithets():
    d = {"epithets": []}
    return jsonify(d)

@app.route('/vocabulary')
def vocabulary():
    v = {"vocabulary": []}
    return jsonify(v)