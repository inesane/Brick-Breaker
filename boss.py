import colorama
from input import input_to, Get
from os import system
import numpy as np
from time import sleep
from colorama import Back, Fore, Style
import config
import time

rows = 40
columns = 80
paddle_char = '='
ball_char = 'O'
left_border = '⎹'
right_border = '⎸'
bottom_border = '‾'
top_border = '_'
brick_length = 4
no_of_bricks = 5
lives = 3
boss_char = '+'

class Boss:
    def __init__(self, Paddle):
        self.x = Paddle.x
        self.y = 1
        self.width = 7
        self.health = 9
        self.defense1 = 0
        self.defense2 = 0
    
    def move(self, Paddle):
        self.x = Paddle.x
    
    def disp(self, arr):
        for i in range(self.width):
            arr[1][self.x + i] = '+'