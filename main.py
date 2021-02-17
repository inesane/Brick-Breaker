import colorama
from input import input_to, Get
from os import system
import numpy as np
from time import sleep
from colorama import Back, Fore, Style

# try:
rows = 30
columns = 80
# fps = 30
# t = 1/fps
paddle_char = '='
ball_char = 'O'
# brick_char = '#'
brick_length = 4
no_of_bricks = 5


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
        if(self.x <= 3 or self.x >= columns-1):
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

    def brick_collision(self, arr, Brick_arr):
        if(self.y > rows or self.y < 1 or self.x < 1 or self.x > columns):
            return
        if((arr[self.y+1][self.x] == '0' or arr[self.y+1][self.x] == '1' or arr[self.y+1][self.x] == '2' or arr[self.y+1][self.x] == '3' or arr[self.y+1][self.x] == '4') and (self.y_vel == -1)):
            curr = int(arr[self.y+1][self.x])
            self.y_vel = 1
            self.y = Brick_arr[curr].y - 1
            if (Brick_arr[curr].strength > 0):
                Brick_arr[curr].strength -= 1
        if((arr[self.y-1][self.x] == '0' or arr[self.y-1][self.x] == '1' or arr[self.y-1][self.x] == '2' or arr[self.y-1][self.x] == '3' or arr[self.y-1][self.x] == '4') and (self.y_vel == 1)):
            curr = int(arr[self.y-1][self.x])
            self.y_vel = -1
            self.y = Brick_arr[curr].y + brick_length
            if (Brick_arr[curr].strength > 0):
                Brick_arr[curr].strength -= 1
        if((arr[self.y][self.x+1] == '0' or arr[self.y][self.x+1] == '1' or arr[self.y][self.x+1] == '2' or arr[self.y][self.x+1] == '3' or arr[self.y][self.x+1] == '4') and (self.x_vel > 0)):
            curr = int(arr[self.y][self.x+1])
            self.x_vel *= -1
            self.x = Brick_arr[curr].x - 1
            if (Brick_arr[curr].strength > 0):
                Brick_arr[curr].strength -= 1
        if((arr[self.y][self.x-1] == '0' or arr[self.y][self.x-1] == '1' or arr[self.y][self.x-1] == '2' or arr[self.y][self.x-1] == '3' or arr[self.y][self.x-1] == '4') and (self.x_vel < 0)):
            curr = int(arr[self.y][self.x-1])
            self.x_vel *= -1
            self.x = Brick_arr[curr].x + brick_length
            if (Brick_arr[curr].strength > 0):
                Brick_arr[curr].strength -= 1


class Brick:
    def __init__(self, index):
        self.x = np.random.randint(3, columns - 4)
        self.y = np.random.randint(3, rows - 10)
        self.strength = np.random.randint(1, 4)
        self.index = index

    def disp(self, arr):
        for i in range(brick_length):
            for j in range(brick_length):
                arr[self.y + j][self.x + i] = self.index


system("stty -echo")
lives = 3
brick_arr = [0]*no_of_bricks
for i in range(no_of_bricks):
    brick_arr[i] = Brick(i)

for k in range(3):
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
        if(not ticks % 3):
            newBall.move()
        ticks += 1
        ticks %= 3

        for i in range(no_of_bricks):
            if(brick_arr[i].strength > 0):
                brick_arr[i].disp(screen)
        newPaddle.disp(screen)
        newBall.disp(screen)

        if(ball_move == 1):
            newBall.paddle_collison(screen, newPaddle)

        newBall.brick_collision(screen, brick_arr)

        if(newBall.y == rows+1):
            lives -= 1
            break
        print("LIVES: ", lives)
        print("TIME: ", )
        print("SCORE: ", )

        print('\033[0;0H')
        # print("\033[H\033[J")

        for i in screen:
            for j in i:
                if(j == '0' or j == '1' or j == '2' or j == '3' or j == '4'):
                    curr = int (j)
                    if(brick_arr[curr].strength == 3):
                        print(Fore.RED + Back.RED, end = "")
                        print(j, end="")
                        print(Style.RESET_ALL, end="")
                    if(brick_arr[curr].strength == 2):
                        print(Fore.YELLOW + Back.YELLOW, end = "")
                        print(j, end="")
                        print(Style.RESET_ALL, end="")
                    if(brick_arr[curr].strength == 1):
                        print(Fore.GREEN + Back.GREEN, end = "")
                        print(j, end="")
                        print(Style.RESET_ALL, end="")
                else:
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
