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
bomb_char = '*'

class Bomb:
    def __init__(self, Boss):
        self.x = Boss.x
        self.y = 2
        self.ticks = 0
    
    def move(self):
        self.ticks += 1
        if(self.ticks%4 == 0):
            self.y += 1
    
    def disp(self, arr):
        if(self.y < rows):
            arr[self.y][self.x] = '*'
        else:
            config.bombs.remove(self)
    
    def hit(self, arr):
        if(arr[self.y+1][self.x] == paddle_char):
            config.bombs.remove(self)
            return True