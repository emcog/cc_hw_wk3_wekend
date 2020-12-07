from flask import render_template
from app import app
from src.x_beats_y import x_beats_y 

@app.route('/')
def index():
    return "Are you ready to Rumble?"


@app.route('/play/<player_1_name>/<player_2_name>/<player_1_choice>/<player_2_choice>')
def play():
    winner = x_beats_y(player_1_name, player_2_name, player_1_choice, player_2_name)
    return f'The winner is {winner}'