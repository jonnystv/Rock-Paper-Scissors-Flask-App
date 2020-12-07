from flask import render_template
from app import app
from app.models.player import *
from app.models.game import *

@app.route("/")
def index():
    return "Hello World!"


@app.route("/<player_1>/<player_2>")
def winning_game_choice(player_1, player_2):
    winner = winning_game_choice(player_1, player_2)
    return winner