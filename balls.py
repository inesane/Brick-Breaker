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

rows = 40
columns = 80
paddle_char = '='
ball_char = 'O'
brick_length = 4
no_of_bricks = 5
lives = 3
left_border = '⎹'
right_border = '⎸'
bottom_border = '‾'
top_border = '_'
boss_char = '+'
bomb_char = '*'


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
        elif(self.x > columns):
            self.x = columns
        if(self.y < 2):
            self.y = 1
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

    def paddle_collison(self, arr, Paddle, time_passed, brick_arr, no_of_total_bricks, ticks):
        if((self.y > rows) or (self.x + abs(self.x_vel)>= columns + 1) or (self.x < 2)):
            return
        else:
            if((arr[self.y+1][self.x] == paddle_char) and (self.y_vel == -1)):
                if(time_passed > 40):
                    for i in range(no_of_total_bricks):
                        brick_arr[i].falling()
                        brick_arr[i].disp(arr)
                self.y_vel = 1
                self.y = rows - 1
                if(Paddle.length % 2 == 0):
                    self.x_vel = -1*((self.x - Paddle.x) - (int)(Paddle.length/2))
                    for i in range (len(config.active_powerups)):
                        if(config.active_powerups[i].active == 1):
                            if(self.x_vel > 0):
                                self.x_vel += 1
                            if(self.x_vel < 0):
                                self.x_vel -= 1
                else:
                    self.x_vel = -1*(Paddle.x + (int)(Paddle.length/2) - self.x)
                    for i in range (len(config.active_powerups)):
                        if(config.active_powerups[i].active == 1):
                            if(self.x_vel > 0):
                                self.x_vel += 1
                            if(self.x_vel < 0):
                                self.x_vel -= 1
            elif((arr[self.y+1][self.x+self.x_vel] == paddle_char) and (self.y_vel == -1)):
                if(time_passed > 40):
                    for i in range(no_of_total_bricks):
                        brick_arr[i].falling()
                        brick_arr[i].disp(arr)
                self.y_vel = 1
                self.y = rows - 1
                self.x += self.x_vel
                if(Paddle.length % 2 == 0):
                    self.x_vel = -1*((self.x - Paddle.x) - (int)(Paddle.length/2))
                    for i in range (len(config.active_powerups)):
                        if(config.active_powerups[i].active == 1):
                            if(self.x_vel > 0):
                                self.x_vel += 1
                            if(self.x_vel < 0):
                                self.x_vel -= 1
                else:
                    self.x_vel = -1*(Paddle.x + (int)(Paddle.length/2) - self.x)
                    for i in range (len(config.active_powerups)):
                        if(config.active_powerups[i].active == 1):
                            if(self.x_vel > 0):
                                self.x_vel += 1
                            if(self.x_vel < 0):
                                self.x_vel -= 1
            if(self.x_vel > 4):
                self.x_vel = 4

    def brick_collision(self, arr, Brick_arr):

        ball_velocities = [self.x_vel, self.y_vel]

        if((self.y > rows) or (self.y < 1) or (self.x < 1) or (self.x + abs(self.x_vel) > columns)):
            return
        
        if((arr[self.y][self.x+1] != ' ') and (arr[self.y][self.x+1] != paddle_char) and (arr[self.y][self.x+1] != left_border) and (arr[self.y][self.x+1] != right_border) and (arr[self.y][self.x+1] != bottom_border) and (arr[self.y][self.x+1] != top_border) and (arr[self.y][self.x+1] != boss_char) and (arr[self.y][self.x+1] != bomb_char) and (self.x_vel > 0)):
            curr = int(arr[self.y][self.x+1])
            self.x = Brick_arr[curr].x - 1
            if(config.fire_ball):
                Brick_arr[curr].explode(arr, Brick_arr, ball_velocities)
            else:
                Brick_arr[curr].collision(arr, Brick_arr, ball_velocities)
            self.x_vel *= -1

        
        elif((arr[self.y][self.x-1] != ' ') and (arr[self.y][self.x-1] != paddle_char) and (arr[self.y][self.x-1] != left_border) and (arr[self.y][self.x-1] != right_border) and (arr[self.y][self.x-1] != bottom_border) and (arr[self.y][self.x-1] != top_border ) and (arr[self.y][self.x-1] != boss_char) and (arr[self.y][self.x-1] != bomb_char) and (self.x_vel < 0)):
            curr = int(arr[self.y][self.x-1])
            self.x = Brick_arr[curr].x + brick_length
            if(config.fire_ball):
                Brick_arr[curr].explode(arr, Brick_arr, ball_velocities)
            else:
                Brick_arr[curr].collision(arr, Brick_arr, ball_velocities)
            self.x_vel *= -1

        
        elif((arr[self.y+1][self.x] != ' ') and (arr[self.y+1][self.x] != paddle_char) and (arr[self.y+1][self.x] != left_border) and (arr[self.y+1][self.x] != right_border) and (arr[self.y+1][self.x] != bottom_border) and (arr[self.y+1][self.x] != top_border) and (arr[self.y+1][self.x] != boss_char) and (arr[self.y+1][self.x] != bomb_char) and (self.y_vel < 0)):
            curr = int(arr[self.y+1][self.x])
            self.y = Brick_arr[curr].y - 1
            if(config.fire_ball):
                Brick_arr[curr].explode(arr, Brick_arr, ball_velocities)
            else:
                Brick_arr[curr].collision(arr, Brick_arr, ball_velocities)
            self.y_vel = 1

        
        elif((arr[self.y-1][self.x] != ' ') and (arr[self.y-1][self.x] != paddle_char) and (arr[self.y-1][self.x] != left_border) and (arr[self.y-1][self.x] != right_border) and (arr[self.y-1][self.x] != bottom_border) and (arr[self.y-1][self.x] != top_border) and (arr[self.y-1][self.x] != boss_char) and (arr[self.y-1][self.x] != bomb_char) and (self.y_vel > 0)):
            curr = int(arr[self.y-1][self.x])
            self.y = Brick_arr[curr].y + brick_length
            if(config.fire_ball):
                Brick_arr[curr].explode(arr, Brick_arr, ball_velocities)
            else:
                Brick_arr[curr].collision(arr, Brick_arr, ball_velocities)
            self.y_vel = -1

    
    def brick_destroy(self, arr, Brick_arr):

        ball_velocities = [self.x_vel, self.y_vel]

        if(self.y > rows or self.y < 1 or self.x < 1 or self.x > columns):
            return
        
        if((arr[self.y][self.x+1] != ' ') and (arr[self.y][self.x+1] != paddle_char) and (arr[self.y][self.x+1] != left_border) and (arr[self.y][self.x+1] != right_border) and (arr[self.y][self.x+1] != bottom_border) and (arr[self.y][self.x+1] != top_border) and (arr[self.y][self.x+1] != boss_char) and (arr[self.y][self.x+1] != bomb_char)  and (self.x_vel > 0)):
            curr = int(arr[self.y][self.x+1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)
        
        elif((arr[self.y][self.x-1] != ' ') and (arr[self.y][self.x-1] != paddle_char) and (arr[self.y][self.x-1] != left_border) and (arr[self.y][self.x-1] != right_border) and (arr[self.y][self.x-1] != bottom_border) and (arr[self.y][self.x-1] != top_border) and (arr[self.y][self.x-1] != boss_char) and (arr[self.y][self.x-1] != bomb_char) and (self.x_vel < 0)):
            curr = int(arr[self.y][self.x-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)
        
        elif((arr[self.y+1][self.x] != ' ') and (arr[self.y+1][self.x] != paddle_char) and (arr[self.y+1][self.x] != left_border) and (arr[self.y+1][self.x] != right_border) and (arr[self.y+1][self.x] != bottom_border) and (arr[self.y+1][self.x] != top_border) and (arr[self.y+1][self.x] != boss_char) and (arr[self.y+1][self.x] != bomb_char) and (self.y_vel < 0)):
            curr = int(arr[self.y+1][self.x])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)
        
        elif((arr[self.y-1][self.x] != ' ') and (arr[self.y-1][self.x] != paddle_char) and (arr[self.y-1][self.x] != left_border) and (arr[self.y-1][self.x] != right_border) and (arr[self.y-1][self.x] != bottom_border) and (arr[self.y-1][self.x] != top_border) and (arr[self.y-1][self.x] != boss_char) and (arr[self.y-1][self.x] != bomb_char) and (self.y_vel > 0)):
            curr = int(arr[self.y-1][self.x])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)
        
    def boss_collision(self, arr, Boss):

        if(arr[self.y-1][self.x] == boss_char):
            self.y_vel *= -1
            Boss.health -= 1
            self.y += 1