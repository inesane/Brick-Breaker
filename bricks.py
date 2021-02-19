import colorama
from input import input_to, Get
from os import system
import numpy as np
from time import sleep
from colorama import Back, Fore, Style
import config

rows = 30
columns = 80
paddle_char = '='
ball_char = 'O'
brick_length = 4
no_of_bricks = 5
lives = 3


class Brick:
    def __init__(self, index):
        # self.x = 0
        # self.y = 0
        self.x = np.random.randint(3, columns - 4)
        self.y = np.random.randint(3, rows - 10)
        self.index = index

    def disp(self, arr):
        for i in range(brick_length):
            for j in range(brick_length):
                if(self.strength == 0):
                    arr[self.y + j][self.x + i] = ' '
                else:
                    arr[self.y + j][self.x + i] = str(self.index)

    def collision(self, arr, Brick_arr):
        if (self.strength > 0):
            if(self.strength == 1):
                config.score += 10
            self.strength -= 1

    def destroy(self):
        if(self.strength > 0):
            self.strength = 0
            config.score += 10


class Unbreakable(Brick):
    pass

    def __init__(self, index):
        self.strength = 100000
        super().__init__(index)


class Breakable(Brick):
    pass

    def __init__(self, index):
        self.strength = np.random.randint(1, 4)
        super().__init__(index)


class Exploding(Brick):
    pass

    def __init__(self, index):
        self.strength = 69
        super().__init__(index)

    def collision(self, arr, Brick_arr):
        self.destroy()
        if((arr[self.y-1][self.x] != ' ') and (arr[self.y-1][self.x] != ball_char)):
            curr = int(arr[self.y-1][self.x])
            Brick_arr[curr].destroy()

        if((arr[self.y][self.x-1] != ' ') and (arr[self.y][self.x-1] != ball_char)):
            curr = int(arr[self.y][self.x-1])
            Brick_arr[curr].destroy()

        if((arr[self.y+brick_length][self.x] != ' ') and (arr[self.y+brick_length][self.x] != ball_char)):
            curr = int(arr[self.y+brick_length][self.x])
            Brick_arr[curr].destroy()

        if((arr[self.y+brick_length-1][self.x-1] != ' ') and (arr[self.y+brick_length-1][self.x-1] != ball_char)):
            curr = int(arr[self.y+brick_length-1][self.x-1])
            Brick_arr[curr].destroy()

        if((arr[self.y][self.x+brick_length] != ' ') and (arr[self.y][self.x+brick_length] != ball_char)):
            curr = int(arr[self.y][self.x+brick_length])
            Brick_arr[curr].destroy()

        if((arr[self.y-1][self.x+brick_length-1] != ' ') and (arr[self.y-1][self.x+brick_length-1] != ball_char)):
            curr = int(arr[self.y-1][self.x+brick_length-1])
            Brick_arr[curr].destroy()

        if((arr[self.y+brick_length][self.x+brick_length-1] != ' ') and (arr[self.y+brick_length][self.x+brick_length-1] != ball_char)):
            curr = int(arr[self.y+brick_length][self.x+brick_length-1])
            Brick_arr[curr].destroy()

        if((arr[self.y+brick_length-1][self.x+brick_length] != ' ') and (arr[self.y+brick_length-1][self.x+brick_length] != ball_char)):
            curr = int(arr[self.y+brick_length-1][self.x+brick_length])
            Brick_arr[curr].destroy()