#!/usr/bin/env python3
import random
from itertools import cycle


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

# moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

win_p1 = 0
win_p2 = 0
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))



""" def game_result(player1, player2):
    win_p1 = 0
    win_p2 = 0
    print(f"player1 {player1} --- player2 {player2}")
    if player1 == player2:
        print("Tie")
        return win_p1, win_p2
    elif beats(player1, player2):
        win_p1 += 1
        print("player1 win")
        return win_p1, win_p2
    else:
        win_p2 += 1
        print("player2 win")
        return win_p1, win_p2

if __name__ == "__main__":
    for i in range(9):
        win_p1, win_p2 = game_result(random.choice(moves), random.choice(moves))
        print(f"\nGame result: Player1 {win_p1} wins. Player2 {win_p2} wins")
        sleep(2)
 """

class Player:
    moves = ['rock', 'paper', 'scissors']

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = None
        self.their_move = 'rock'

    def  learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        return self.their_move


class RockPlayer(Player):
    def move(self):
        return 'rock'


class CyclePlayer(Player):
    def __init__(self):
        self.moves_cycle = cycle(self.moves)

    def move(self):
        return next(self.moves_cycle)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(9):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    players = [RandomPlayer(), ReflectPlayer(), CyclePlayer(), RockPlayer()]
    game = Game(CyclePlayer(), ReflectPlayer())
    game.play_game()
