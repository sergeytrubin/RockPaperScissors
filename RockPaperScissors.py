#!/usr/bin/env python3
import random
from itertools import cycle
import os
os.system('')  # enable VT100 Escape Sequence for WINDOWS 10

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


"""The Player class is the parent class for all of the Players
in this game"""


# class template for other player classes
class Player:
    moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass  # method template for player class that need to remember moves


# Human player class - moves according to user input
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


# Player moves are random choises from the list of moves
class RandomPlayer(Player):
    def learn(self, my_move, their_move):
        # This class don't need to remember anything
        pass

    def move(self):
        return random.choice(self.moves)


# Player plays the last play of his opponent
class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = None
        self.their_move = 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        return self.their_move


# Player always plays a rock
class RockPlayer(Player):
    def learn(self, my_move, their_move):
        # This class don't need to remember anything
        pass

    def move(self):
        return 'rock'


# Player cycles through the list of moves
class CyclePlayer(Player):
    def __init__(self):
        self.moves_cycle = cycle(self.moves)

    def learn(self, my_move, their_move):
        # This class don't need to remember anything
        pass

    def move(self):
        return next(self.moves_cycle)


# Function to check who wins
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


# Function to print description of the winning move
def beats_desc(one, two):
    CHD = '\033[91m'
    CEND = '\033[0m'
    if (one == 'rock' and two == 'scissors'):
        print(CHD + "Rock crushes Scissors" + CEND)
    elif (one == 'scissors' and two == 'paper'):
        print(CHD + "Scissors cuts Paper" + CEND)
    elif (one == 'paper' and two == 'rock'):
        print(CHD + "Paper covers Rock" + CEND)
    elif (one == 'rock' and two == 'lizard'):
        print(CHD + "Rock crushes Lizard" + CEND)
    elif (one == 'lizard' and two == 'spock'):
        print(CHD + "Lizard poisons Spock" + CEND)
    elif (one == 'spock' and two == 'scissors'):
        print(CHD + "Spock smashes Scissors" + CEND)
    elif (one == 'scissors' and two == 'lizard'):
        print(CHD + "Scissors decapitates Lizard" + CEND)
    elif (one == 'lizard' and two == 'paper'):
        print(CHD + "Lizard eats Paper" + CEND)
    elif (one == 'paper' and two == 'spock'):
        print(CHD + "Paper disproves Spock" + CEND)
    elif (one == 'spock' and two == 'rock'):
        print(CHD + "Spock vaporizes Rock" + CEND)


# Function to check who wins
def game_result(player1, player2, win_p1, win_p2):
    if player1 == player2:
        print('\033[93m' + '** TIE! **' + '\033[0m')
        return win_p1, win_p2
    elif beats(player1, player2):
        win_p1 += 1
        beats_desc(player1, player2)
        print('\033[32m' + '** PLAYER ONE WINS! **' + '\033[0m')
        return win_p1, win_p2
    else:
        win_p2 += 1
        beats_desc(player2, player1)
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


# Game class that defines the game flow.
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
        CHD = "\033[96m"
        CEND = "\033[00m"
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("You played:" + CHD + f"{move1}" + CEND)
        print("Opponent played:" + CHD + f"{move2}" + CEND)
        self.w1, self.w2 = game_result(move1, move2, self.w1, self.w2)
        print(f"Score: Player One {self.w1}, Player Two {self.w2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        CHD = "\033[95m"
        CEND = "\033[00m"
        print(CHD + "GAME START!" + CEND)
        self.select_game_mode()
        for round in range(self.game_mode):
            print(f"\nRound {round} --")
            self.play_round()
        if self.w1 > self.w2:
            print(CHD + '** THE WINNER IS PLAYER 1**' + CEND)
        elif self.w1 < self.w2:
            print(CHD + '** THE WINNER IS PLAYER 2**' + CEND)
        else:
            print(CHD + "** IT'S A TIE!**" + CEND)
        print(CHD + "GAME OVER!" + CEND)


if __name__ == '__main__':
    players = [RandomPlayer(), ReflectPlayer(), RockPlayer(), CyclePlayer()]
    game = Game(HumanPlayer(), random.choice(players))
    game.play_game()
