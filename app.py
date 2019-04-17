#! python3

from flask import Flask, jsonify
import os
from dotenv import load_dotenv

project_root = os.path.dirname("./")
env_path = os.path.join(project_root, ".env")
load_dotenv(dotenv_path=env_path, verbose=True, override=True)

app = Flask(__name__)

@app.route('/')
def generate_epithets():
    d = {"epithets": []}
    return jsonify(d)

@app.route('/vocabulary')
def vocabulary():
    v = {"vocabulary": []}
    return jsonify(v)