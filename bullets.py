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

class Bullet:
    def __init__(self,x):
        self.x = x
        self.y = rows - 1
        self.y_vel = -1
        self.ticks = 0

    def move(self):
        self.ticks+=1
        if(self.ticks%4 == 0):
            self.y += self.y_vel

    def disp(self, arr):
        if(self.y>=2):
            arr[self.y][self.x] = '.'
        if(self.y<2):
            config.bullets.remove(self)
    
    def collision(self, arr, Brick_arr):
        if((arr[self.y-1][self.x] != ' ') and (arr[self.y-1][self.x] != paddle_char) and (arr[self.y-1][self.x] != left_border) and (arr[self.y-1][self.x] != right_border) and (arr[self.y-1][self.x] != bottom_border) and (arr[self.y-1][self.x] != top_border)):
            curr = int(arr[self.y-1][self.x])
            ball_velocities = [0,0]
            Brick_arr[curr].collision(arr, Brick_arr, ball_velocities)
            config.bullets.remove(self)