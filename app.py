#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")
# write 'hello world' to the console
print('Juego de piedra, papel o tijeras hecha en colaboración con Copilot')
def get_choice(player):
    while True:
        print(f"Turno de {player}")
        choice = input("Elige piedra, papel o tijeras: ").lower()
        if choice in ['piedra', 'papel', 'tijeras']:
            return choice

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return 0
    elif (choice1 == 'piedra' and choice2 == 'tijeras') or (choice1 == 'papel' and choice2 == 'piedra') or (choice1 == 'tijeras' and choice2 == 'papel'):
        return 1
    else:
        return 2

def play_round(player1, player2):
    choice1 = get_choice(player1)
    choice2 = get_choice(player2)
    return determine_winner(choice1, choice2)

def play_game(player1, player2):
    scores = {player1: 0, player2: 0}
    while True:
        result = play_round(player1, player2)
        if result == 1:
            scores[player1] += 1
        elif result == 2:
            scores[player2] += 1
        print(f"Puntuaciones: {player1} - {scores[player1]}, {player2} - {scores[player2]}")
        play_again = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if play_again != 's':
            break
    print("Fin del juego")

play_game('Jugador 1', 'Jugador 2')
