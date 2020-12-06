from flask import render_template
from app import app
import random

@app.route('/')
def index():
    return "Are you ready to Rumble?"


@app.route('/random')
def random():
    random_int = random.randint(1, 3)
    return random_int