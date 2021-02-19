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


class PowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_vel = -1

    def move(self):
        if(self.y < rows):
            self.y += self.y_vel

    def disp(self, arr):
        arr[self.y][self.x] = 'e'
        arr[self.y][self.x] = 'p'
