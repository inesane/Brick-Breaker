import colorama
from input import input_to, Get
from os import system
import numpy as np
from time import sleep

# try:
rows = 30
columns = 80
# fps = 30
# t = 1/fps
paddle_char = '='
ball_char = 'O'


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
        if((self.x + self.length >= columns+1) and (key == "d")):
            return
        if(self.x <= 2 and key == "a"):
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
        if(self.x < 2):
            arr[self.y][2] = ball_char
        elif(self.x > columns):
            arr[self.y][columns] = ball_char
        else:
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
        if(self.x <= 3 or self.x >= columns-1):
            self.x_vel = -1*self.x_vel

    def paddle_collison(self, arr, Paddle):
        if(self.y > rows):
            return
        if((arr[self.y+1][self.x] == paddle_char) and (self.y_vel == -1)):
            self.y_vel = 1
            self.y = rows - 1
            if(Paddle.length % 2 == 0):
                self.x_vel = ((self.x - Paddle.x) - (int)(Paddle.length/2))
            else:
                self.x_vel = (Paddle.x + (int)(Paddle.length/2) - self.x)

system("stty -echo")
lives = 3

for j in range(3):
    newPaddle = Paddle(9)
    newBall = Ball(newPaddle)
    ball_move = 0
    ticks = 3

    while True:
        key = input_to(Get())

        screen = np.full((rows+2, columns+3), " ")
        for i in range(rows+2):
            screen[i][0] = '⎹'
            screen[i][columns+1] = '⎸'
            screen[i][columns+2] = '\n'

        for i in range(columns+2):
            screen[0][i] = '_'
            screen[rows+1][i] = '‾'

        screen[0][0] = ' '
        screen[rows+1][0] = ' '
        screen[0][columns+1] = ' '
        screen[rows+1][columns+1] = ' '
        if(not ticks%3):
            newBall.move()
        ticks+=1
        ticks%=3
        
        newPaddle.disp(screen)
        newBall.disp(screen)

        if(ball_move == 1):
            newBall.paddle_collison(screen, newPaddle)

        if(newBall.y == rows+1):
            lives -= 1
            break
        print("LIVES: ", lives)

        print('\033[0;0H')
        # print("\033[H\033[J")

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
            system("stty echo")
            quit()
        # sleep(0.05)

print("GAME OVER")

# except:
system("stty echo")
