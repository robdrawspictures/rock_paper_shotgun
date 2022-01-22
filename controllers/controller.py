from flask import render_template, request
import random
from models.game import Game
from models.player import Player
from models.current_players import add_new_player, players
from rps import app

@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/stage2", methods=["POST"])
def choice_1():
    name = request.form['name']
    choice = request.form['choice']
    new_player1 = Player(name, choice)
    add_new_player(new_player1)
    return render_template("stage2.html", player1 = new_player1)

@app.route("/result", methods=['POST'])
def result():
    name = request.form['name']
    choice = request.form['choice']
    player1 = players[0]
    player2 = Player(name, choice)
    game = Game(player1, player2)
    outcome = game.play_game()
    players.clear()
    return render_template("result.html", player1 = player1, player2 = player2, outcome = outcome)

@app.route("/play")
def play():
    return render_template("play.html")

@app.route("/comp_result", methods=['POST'])
def vs_comp():
    choices = ["rock", "paper", "scissors"]
    name = request.form['name']
    choice = request.form['choice']
    player1 = Player(name, choice)
    player2 = Player("Computer", random.choice(choices))
    game = Game(player1, player2)
    outcome = game.play_game()
    return render_template("comp_result.html", player1=player1, player2=player2, outcome=outcome)
