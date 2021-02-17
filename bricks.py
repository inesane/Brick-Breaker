import colorama
from input import input_to, Get
from os import system
import numpy as np
from time import sleep
from colorama import Back, Fore, Style

rows = 30
columns = 80
paddle_char = '='
ball_char = 'O'
brick_length = 4
no_of_bricks = 5
lives = 3

class Brick:
    def __init__(self, index):
        self.x = np.random.randint(3, columns - 4)
        self.y = np.random.randint(3, rows - 10)
        self.strength = np.random.randint(1, 4)
        self.index = index

    def disp(self, arr):
        for i in range(brick_length):
            for j in range(brick_length):
                arr[self.y + j][self.x + i] = self.index