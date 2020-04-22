#!/usr/bin/env python3
import random
from itertools import cycle
import os
os.system('') #enable VT100 Escape Sequence for WINDOWS 10

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        # method template for players classes that need to remember moves
        pass


class HumanPlayer(Player):
    def __init__(self):
        self.human_move = ''

    def learn(self, my_move, their_move):
        # This class don't need to remember anything
        pass

    def move(self):
        self.human_move = input(" ,".join(self.moves) + " > ").lower()
        while self.human_move not in self.moves:
            self.human_move = input(" ,".join(self.moves) + " > ").lower()
        return self.human_move


class RandomPlayer(Player):
    def learn(self, my_move, their_move):
        # This class don't need to remember anything
        pass

    def move(self):
        return random.choice(self.moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = None
        self.their_move = 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        return self.their_move


class RockPlayer(Player):
    def learn(self, my_move, their_move):
        # This class don't need to remember anything
        pass

    def move(self):
        return 'rock'


class CyclePlayer(Player):
    def __init__(self):
        self.moves_cycle = cycle(self.moves)

    def learn(self, my_move, their_move):
        # This class don't need to remember anything
        pass

    def move(self):
        return next(self.moves_cycle)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock') or
            (one == 'rock' and two == 'lizard') or
            (one == 'lizard' and two == 'spock') or
            (one == 'spock' and two == 'scissors') or
            (one == 'scissors' and two == 'lizard') or
            (one == 'lizard' and two == 'paper') or
            (one == 'paper' and two == 'spock') or
            (one == 'spock' and two == 'rock'))


def game_result(player1, player2, win_p1, win_p2):
    if player1 == player2:
        print('\033[93m' + '** TIE! **' + '\033[0m')
        return win_p1, win_p2
    elif beats(player1, player2):
        win_p1 += 1
        print('\033[32m' + '** PLAYER ONE WINS! **' + '\033[0m')
        return win_p1, win_p2
    else:
        win_p2 += 1
        print('\033[31m' + '** PLAYER TWO WINS! **' + '\033[0m')
        return win_p1, win_p2


# Check that user input is correct
def verify_user_input(choice_range):
    c = [x for x in range(1, choice_range + 1)]
    while True:
        user_input = input(f"Make a choice ({c[0]}-{c[len(c)-1]}) > ")
        try:
            if int(user_input) not in c:
                print('Please choose the game mode > ')
            else:
                return int(user_input)
        except ValueError:
            print('Please choose the game mode > ')


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.w1 = 0
        self.w2 = 0
        self.choice = None
        self.game_mode = ''

    def select_game_mode(self):
        print('Please choose the game mode: ')
        print('1. Single Round.')
        print('2. Best of Three.')
        print('3. Custom Number of Rounds.')
        self.choice = verify_user_input(3)
        if self.choice == 1:
            self.game_mode = 1
        elif self.choice == 2:
            self.game_mode = 3
        elif self.choice == 3:
            while not self.game_mode.isnumeric():
                self.game_mode = input('Enter number of rounds > ')
            self.game_mode = int(self.game_mode)

    def play_round(self):
        hd = "\033[96m"
        cend = "\033[00m"
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("You played:" + hd + f"{move1}" + cend)
        print("Opponent played:" + hd + f"{move2}" + cend)
        self.w1, self.w2 = game_result(move1, move2, self.w1, self.w2)
        print(f"Score: Player One {self.w1}, Player Two {self.w2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        hd = "\033[95m"
        cend = "\033[00m"
        print(hd + "GAME START!" + cend)
        self.select_game_mode()
        for round in range(self.game_mode):
            print(f"\nRound {round} --")
            self.play_round()
        if self.w1 > self.w2:
            print(hd + '** THE WINNER IS PLAYER 1**' + cend)
        elif self.w1 < self.w2:
            print(hd + '** THE WINNER IS PLAYER 2**' + cend)
        else:
            print(hd + "** IT'S A TIE!**" + cend)
        print(hd + "GAME OVER!" + cend)


if __name__ == '__main__':
    players = [RandomPlayer(), ReflectPlayer(), RockPlayer(), CyclePlayer()]
    game = Game(HumanPlayer(), random.choice(players))
    game.play_game()
