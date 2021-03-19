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
brick_length = 4
no_of_bricks = 5
lives = 3

class PowerUp:
    def __init__(self, x, y, ball_velocities):
        self.x = x
        self.y = y
        self.y_vel_init = ball_velocities[1]
        self.x_vel = ball_velocities[0]
        self.y_vel = 1
        self.ticks = 0
        self.active = 0
        self.time = time.time()
        self.moved = 3

    def move(self):
        if((self.y_vel_init < 0) and (self.moved > 0)):
            self.ticks += 1
            if(self.ticks % 4 == 0):
                self.y += self.y_vel_init
                self.x += self.x_vel
                self.moved -= 1
            return True
        else:
            self.y_vel = 1
            if(self.x <= 2 and self.x_vel < 0):
                self.x_vel = -1*self.x_vel
                self.x = 2
            if(self.x >= columns - 1 and self.x_vel > 0):
                self.x_vel = -1*self.x_vel
                self.x = columns - 1
            if(self.y < 2 and self.y_vel < 0):
                self.y = 1
                self.y_vel = 1
            if(self.y < rows):
                self.ticks += 1
                if(self.ticks % 4 == 0):
                    self.y += self.y_vel
                    self.x += self.x_vel
                return True
            if(self.y >= rows):
                config.falling_powerups.remove(self)
                return False
        # self.ticks+=1
        # if(self.ticks % 4 == 0):
        #     self.y += self.y_vel_init
        #     self.x += self.x_vel
        #     self.y_vel_init += 1
        # if(self.x <= 2 and self.x_vel < 0):
        #     self.x_vel = -1*self.x_vel
        #     self.x = 2
        # if(self.x >= columns - 1 and self.x_vel > 0):
        #     self.x_vel = -1*self.x_vel
        #     self.x = columns - 1
        # if(self.y < 2 and self.y_vel_init < 0):
        #     self.y = 1
        #     self.y_vel_init *= -1

        # if(self.y < rows):
        #     return True
        # if(self.y >= rows):
        #     config.falling_powerups.remove(self)
        #     return False

    
    def caught(self, arr):
        if(arr[self.y+1][self.x] == paddle_char or arr[self.y+1][self.x+1] == paddle_char):
            config.active_powerups.append(self)
            config.falling_powerups.remove(self)
    

class ExpandPaddle(PowerUp):
    pass

    def __init__(self, x, y, ball_velocities):
        self.which = 1
        super().__init__(x, y, ball_velocities)


    def disp(self, arr):
        if(self.x < 2 and self.x_vel < 0):
            self.x = 2
        elif(self.x > columns - 1 and self.x_vel > 0):
            self.x = columns - 1
        # if(self.y )
        arr[self.y][self.x] = 'e'
        arr[self.y][self.x+1] = 'p'


class ShrinkPaddle(PowerUp):
    pass

    def __init__(self, x, y, ball_velocities):
        self.which = 2
        super().__init__(x, y, ball_velocities)

    def disp(self, arr):
        if(self.x < 2 and self.x_vel < 0):
            self.x = 2
        elif(self.x > columns - 1 and self.x_vel > 0):
            self.x = columns - 1
        arr[self.y][self.x] = 's'
        arr[self.y][self.x+1] = 'p'


class FireBall(PowerUp):
    pass

    def __init__(self, x, y, ball_velocities):
        self.which = 3
        super().__init__(x, y, ball_velocities)

    def disp(self, arr):
        if(self.x < 2 and self.x_vel < 0):
            self.x = 2
        elif(self.x > columns - 1 and self.x_vel > 0):
            self.x = columns - 1
        arr[self.y][self.x] = 'f'
        arr[self.y][self.x+1] = 'i'


class FastBall(PowerUp):
    pass

    def __init__(self, x, y, ball_velocities):
        self.which = 4
        super().__init__(x, y, ball_velocities)

    def disp(self, arr):
        if(self.x < 2 and self.x_vel < 0):
            self.x = 2
        elif(self.x > columns - 1 and self.x_vel > 0):
            self.x = columns - 1
        arr[self.y][self.x] = 'f'
        arr[self.y][self.x+1] = 'b'


class ThroughBall(PowerUp):
    pass

    def __init__(self, x, y, ball_velocities):
        self.which = 5
        super().__init__(x, y, ball_velocities)

    def disp(self, arr):
        if(self.x < 2 and self.x_vel < 0):
            self.x = 2
        elif(self.x > columns - 1 and self.x_vel > 0):
            self.x = columns - 1
        arr[self.y][self.x] = 't'
        arr[self.y][self.x+1] = 'b'


class ShootingPaddle(PowerUp):
    pass

    def __init__(self, x, y, ball_velocities):
        self.which = 6
        super().__init__(x, y, ball_velocities)

    def disp(self, arr):
        if(self.x < 2 and self.x_vel < 0):
            self.x = 2
        elif(self.x > columns - 1 and self.x_vel > 0):
            self.x = columns - 1
        arr[self.y][self.x] = 's'
        arr[self.y][self.x+1] = 'h'