import colorama
from input import input_to, Get
from os import system
import numpy as np
from time import sleep
from colorama import Back, Fore, Style
from paddles import Paddle
from bricks import Brick
from powerups import PowerUp
import config

rows = 30
columns = 80
paddle_char = '='
ball_char = 'O'
brick_length = 4
no_of_bricks = 5
lives = 3


class Ball:
    def __init__(self, Paddle):
        self.y = Paddle.y-2
        self.x = np.random.randint(Paddle.x, Paddle.x+Paddle.length)
        self.start_pos = self.x - Paddle.x
        self.x_vel = 0
        self.y_vel = 0

    def disp(self, arr):
        if(self.x < 2):
            self.x = 2
            # self.x_vel *= -1
        elif(self.x > columns):
            self.x = columns
            # self.x_vel *= 1
        if(self.y < 2):
            self.y = 1
            # self.y_vel = -1
        arr[self.y][self.x] = ball_char

    def before_start_move(self, Paddle):
        self.x = Paddle.x + self.start_pos

    def start_move(self):
        self.y_vel = 1

    def move(self):
        self.y -= self.y_vel
        self.x += self.x_vel
        if(self.y == 1):
            self.y_vel = -1*self.y_vel
        if(self.x <= 2 or self.x >= columns):
            self.x_vel = -1*self.x_vel

    def paddle_collison(self, arr, Paddle):
        if(self.y > rows):
            return
        if((arr[self.y+1][self.x] == paddle_char) and (self.y_vel == -1)):
            self.y_vel = 1
            self.y = rows - 1
            if(Paddle.length % 2 == 0):
                self.x_vel = -1*((self.x - Paddle.x) - (int)(Paddle.length/2))
            else:
                self.x_vel = -1*(Paddle.x + (int)(Paddle.length/2) - self.x)
        elif((arr[self.y+1][self.x+self.x_vel] == paddle_char) and (self.y_vel == -1)):
            if(self.x+self.x_vel>columns):
                return
            self.y_vel = 1
            self.y = rows - 1
            self.x += self.x_vel
            if(Paddle.length % 2 == 0):
                self.x_vel = -1*((self.x - Paddle.x) - (int)(Paddle.length/2))
            else:
                self.x_vel = -1*(Paddle.x + (int)(Paddle.length/2) - self.x)

    def brick_collision(self, arr, Brick_arr):
        if(self.y > rows or self.y < 1 or self.x < 1 or self.x > columns):
            return
        if((arr[self.y][self.x+1] == '0' or arr[self.y][self.x+1] == '1' or arr[self.y][self.x+1] == '2' or arr[self.y][self.x+1] == '3' or arr[self.y][self.x+1] == '4') and (self.x_vel > 0)):
            curr = int(arr[self.y][self.x+1])
            self.x_vel *= -1
            self.x = Brick_arr[curr].x - 1
            if (Brick_arr[curr].strength > 0):
                if(Brick_arr[curr].strength == 1):
                    config.score += 10
                    # rand = np.random.randint(1,10)
                    # if(rand%3 == 0):
                    #     PowerUp(Brick_arr[curr].x, Brick_arr[curr].y, arr)
                Brick_arr[curr].strength -= 1
        elif((arr[self.y][self.x-1] == '0' or arr[self.y][self.x-1] == '1' or arr[self.y][self.x-1] == '2' or arr[self.y][self.x-1] == '3' or arr[self.y][self.x-1] == '4') and (self.x_vel < 0)):
            curr = int(arr[self.y][self.x-1])
            self.x_vel *= -1
            self.x = Brick_arr[curr].x + brick_length
            if (Brick_arr[curr].strength > 0):
                if(Brick_arr[curr].strength == 1):
                    config.score += 10
                    # rand = np.random.randint(1,10)
                    # if(rand%3 == 0):
                    #     PowerUp(Brick_arr[curr].x, Brick_arr[curr].y, arr)
                Brick_arr[curr].strength -= 1
        elif((arr[self.y+1][self.x] == '0' or arr[self.y+1][self.x] == '1' or arr[self.y+1][self.x] == '2' or arr[self.y+1][self.x] == '3' or arr[self.y+1][self.x] == '4') and (self.y_vel == -1)):
            curr = int(arr[self.y+1][self.x])
            self.y_vel = 1
            self.y = Brick_arr[curr].y - 1
            if (Brick_arr[curr].strength > 0):
                if(Brick_arr[curr].strength == 1):
                    config.score += 10
                    # rand = np.random.randint(1,10)
                    # if(rand%3 == 0):
                    #     PowerUp(Brick_arr[curr].x, Brick_arr[curr].y, arr)
                Brick_arr[curr].strength -= 1
        elif((arr[self.y-1][self.x] == '0' or arr[self.y-1][self.x] == '1' or arr[self.y-1][self.x] == '2' or arr[self.y-1][self.x] == '3' or arr[self.y-1][self.x] == '4') and (self.y_vel == 1)):
            curr = int(arr[self.y-1][self.x])
            self.y_vel = -1
            self.y = Brick_arr[curr].y + brick_length
            if (Brick_arr[curr].strength > 0):
                if(Brick_arr[curr].strength == 1):
                    config.score += 10
                    # rand = np.random.randint(1,10)
                    # if(rand%3 == 0):
                    #     PowerUp(Brick_arr[curr].x, Brick_arr[curr].y, arr)
                Brick_arr[curr].strength -= 1