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
brick_length = 4
no_of_bricks = 5
lives = 3

class PowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_vel = 1
        self.ticks = 0
        self.active = 0
        self.time = time.time()

    def move(self):
        if(self.y < rows):
            self.ticks += 1
            if(self.ticks % 4 == 0):
                self.y += self.y_vel
            return True
        if(self.y >= rows):
            config.falling_powerups.remove(self)
            return False
    
    def caught(self, arr):
        if(arr[self.y+1][self.x] == paddle_char or arr[self.y+1][self.x+1] == paddle_char):
            config.active_powerups.append(self)
            config.falling_powerups.remove(self)


class ExpandPaddle(PowerUp):
    pass

    def __init__(self, x, y):
        self.which = 1
        super().__init__(x, y)


    def disp(self, arr):
        arr[self.y][self.x] = 'e'
        arr[self.y][self.x+1] = 'p'


class ShrinkPaddle(PowerUp):
    pass

    def __init__(self, x, y):
        self.which = 2
        super().__init__(x, y)

    def disp(self, arr):
        arr[self.y][self.x] = 's'
        arr[self.y][self.x+1] = 'p'


class BallMultiplier(PowerUp):
    pass

    def __init__(self, x, y):
        self.which = 3
        super().__init__(x, y)

    def disp(self, arr):
        arr[self.y][self.x] = 'b'
        arr[self.y][self.x+1] = 'm'


class FastBall(PowerUp):
    pass

    def __init__(self, x, y):
        self.which = 4
        super().__init__(x, y)

    def disp(self, arr):
        arr[self.y][self.x] = 'f'
        arr[self.y][self.x+1] = 'b'


class ThroughBall(PowerUp):
    pass

    def __init__(self, x, y):
        self.which = 5
        super().__init__(x, y)

    def disp(self, arr):
        arr[self.y][self.x] = 't'
        arr[self.y][self.x+1] = 'b'


class PaddleGrab(PowerUp):
    pass

    def __init__(self, x, y):
        self.which = 6
        super().__init__(x, y)

    def disp(self, arr):
        arr[self.y][self.x] = 'p'
        arr[self.y][self.x+1] = 'g'