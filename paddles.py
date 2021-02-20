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


class Paddle:
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.x = 10
        self.y = rows+1
        self.vel = 1

    def disp(self, arr):
        for i in range(self.x, self.x+self.length):
            arr[self.y-1][i] = paddle_char

    def move(self, key):
        if((self.x + self.length >= columns + 1) and (key == "d")):
            return
        if(self.x <= 2 and key == "a"):
            return
        else:
            if(key == "a"):
                self.x -= 1
            elif (key == "d"):
                self.x += 1