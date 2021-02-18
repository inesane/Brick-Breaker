import colorama
from input import input_to, Get
from os import system
import numpy as np
from time import sleep
from colorama import Back, Fore, Style
from paddles import Paddle
from bricks import Brick
from balls import Ball
import time
import config

# try:
rows = 30
columns = 80
paddle_char = '='
ball_char = 'O'
brick_length = 4
no_of_bricks = 5
lives = 3
ball_speed = 3
initial_time = time.time()

system("stty -echo")
brick_arr = [0]*no_of_bricks
for i in range(no_of_bricks):
    brick_arr[i] = Brick(str(i))

# brick_arr[0].x = np.random.randint(3, 7)
# brick_arr[0].y = np.random.randint(3, 8)
# brick_arr[1].x = np.random.randint(11, 15)
# brick_arr[1].y = np.random.randint(3, 8)
# brick_arr[2].x = np.random.randint(19, 23)
# brick_arr[2].y = np.random.randint(3, 8)
# brick_arr[3].x = np.random.randint(27, 31)
# brick_arr[3].y = np.random.randint(3, 8)
# brick_arr[4].x = np.random.randint(35, 39)
# brick_arr[4].y = np.random.randint(3, 8)
# brick_arr[5].x = np.random.randint(43, 47)
# brick_arr[5].y = np.random.randint(3, 8)

unbreakable = np.random.randint(0, no_of_bricks)
brick_arr[unbreakable].strength = 1000

for k in range(3):
    newPaddle = Paddle(7)
    newBall = Ball(newPaddle)
    ball_move = 0
    ticks = 3

    while True:
        time_played = time.time()
        key = input_to(Get())

        screen = np.full((rows+2, columns+3), " ", dtype=np.dtype('U100'))

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
        if(not ticks % ball_speed):
            newBall.move()
        ticks += 1

        for i in range(no_of_bricks):
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
        print("TIME:  ", round(time_played - initial_time))
        print("SCORE: ", config.score)

        print('\033[0;0H')
        # print("\033[H\033[J")

        curr_row = -1
        for i in screen:
            curr_row += 1
            curr_col = -1
            for j in i:
                curr_col += 1
                if(j == '0' or j == '1' or j == '2' or j == '3' or j == '4'or j == '5'or j == '6'or j == '7'or j == '8'or j == '9'or j == '10'):
                    curr = int (j)
                    if(brick_arr[curr].strength > 3):
                        print(Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX, end = "")
                        print(' ', end="")
                        print(Style.RESET_ALL, end="")
                    if(brick_arr[curr].strength == 3):
                        print(Fore.RED + Back.RED, end = "")
                        print(' ', end="")
                        print(Style.RESET_ALL, end="")
                    if(brick_arr[curr].strength == 2):
                        print(Fore.YELLOW + Back.YELLOW, end = "")
                        print(' ', end="")
                        print(Style.RESET_ALL, end="")
                    if(brick_arr[curr].strength == 1):
                        print(Fore.GREEN + Back.GREEN, end = "")
                        print(' ', end="")
                        print(Style.RESET_ALL, end="")
                    if(brick_arr[curr].strength == 0):
                        print(' ', end="")
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