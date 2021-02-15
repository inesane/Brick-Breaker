import colorama
import copy

from input import input_to, Get

import numpy as np

rows = 30
columns = 30
# fps = 30
# t = 1/fps
paddle_char = '='
ball_char = 'O'


class Paddle:
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.x = 10
        self.y = rows
        self.vel = 1

    def disp(self, arr):
        for i in range(self.x, self.x+self.length):
            arr[self.y-1][i] = paddle_char

    def move(self, key):
        if((self.x + self.length >= columns) and (key == "d")):
            return
        if(self.x <= 0 and key == "a"):
            return
        else:
            if(key == "a"):
                self.x -= 1
            elif (key == "d"):
                self.x += 1


class Ball:
    def __init__(self, Paddle):
        self.y = Paddle.y-2
        self.x = np.random.randint(Paddle.x, Paddle.x+Paddle.length)
        self.start_pos = self.x - Paddle.x
        self.x_vel = 0
        self.y_vel = 0

    def disp(self, arr):
        arr[self.y][self.x] = ball_char

    def before_start_move(self, Paddle):
        self.x = Paddle.x + self.start_pos

    def start_move(self):
        self.y_vel = 1

    def move(self):
        self.y -= self.y_vel
        self.x -= self.x_vel
        if(self.y == 1):
            self.y_vel = -1*self.y_vel
        if(self.x <= 2 or self.x >= columns):
            self.x_vel = -1*self.x_vel
        if(self.y == rows+1):
            print("GAME OVER")
            quit()

    def paddle_collison(self, arr, Paddle):
        if((arr[self.y+1][self.x] == paddle_char) and (self.y_vel == -1)):
            self.y_vel = 1
            if(Paddle.length % 2 == 0):
                self.x_vel = ((self.x - Paddle.x) - (Paddle.length/2))
                print(self.x)
                print(Paddle.x)
                print(Paddle.length/2)

            else:
                self.x_vel = (Paddle.x + (int)(Paddle.length/2) - self.x)


newPaddle = Paddle(6)
newBall = Ball(newPaddle)
ball_move = 0

while True:
    key = input_to(Get())

    screen = np.full((rows+2, columns+4), " ")
    for i in range(rows+2):
        screen[i][0] = '⎹'
        screen[i][columns+2] = '⎸'
        screen[i][columns+3] = '\n'

    for i in range(columns+3):
        screen[0][i] = '_'
        screen[rows+1][i] = '‾'

    screen[0][0] = ' '
    screen[rows+1][0] = ' '
    screen[0][columns+2] = ' '
    screen[rows+1][columns+2] = ' '
    print("\033[H\033[J", end="")

    newPaddle.disp(screen)

    newBall.disp(screen)
    newBall.move()
    if(ball_move == 1):
        newBall.paddle_collison(screen, newPaddle)

    for i in screen:
        for j in i:
            print(j, end="")

    if(key == "d" or key == "a"):
        newPaddle.move(key)
        if(ball_move == 0):
            newBall.before_start_move(newPaddle)

    if(key == "w" and ball_move == 0):
        newBall.start_move()
        ball_move = 1

    if(key == "x"):
        quit()