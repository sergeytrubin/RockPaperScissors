#!/usr/bin/env python3
import random
from itertools import cycle


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

# moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


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
    pass


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
    players = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    game = Game(CyclePlayer(), RandomPlayer())
    game.play_game()
