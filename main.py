import colorama
from input import input_to, Get
from os import system
import numpy as np
from time import sleep
from colorama import Back, Fore, Style
from paddles import Paddle
from bricks import Brick
from balls import Ball

# try:
rows = 30
columns = 80
paddle_char = '='
ball_char = 'O'
# brick_char = '#'
brick_length = 4
no_of_bricks = 5
lives = 3

system("stty -echo")
brick_arr = [0]*no_of_bricks
for i in range(no_of_bricks):
    brick_arr[i] = Brick(i)

unbreakable = np.random.randint(0, no_of_bricks)
brick_arr[unbreakable].strength = 1000

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

        if(ball_move == 1):
            newBall.paddle_collison(screen, newPaddle)

        newBall.brick_collision(screen, brick_arr)

        newBall.disp(screen)


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
                    if(brick_arr[curr].strength > 3):
                        print(Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX, end = "")
                        print(j, end="")
                        print(Style.RESET_ALL, end="")
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