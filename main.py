import colorama
from input import input_to, Get
from os import system
import numpy as np
from time import sleep
from colorama import Back, Fore, Style
from paddles import Paddle
from bricks import Unbreakable, Breakable, Exploding
from balls import Ball
import time
import config

# try:
rows = 30
columns = 80
paddle_char = '='
ball_char = 'O'
brick_length = 4
no_of_breakable_bricks = 6
no_of_unbreakable_bricks = 2
no_of_exploding_bricks = 4
lives = 3
ball_speed = 3
initial_time = time.time()
left_border = '⎹'
right_border = '⎸'
bottom_border = '‾'
top_border = '_'

system("stty -echo")
brick_arr = [0]*(no_of_breakable_bricks+no_of_unbreakable_bricks + no_of_exploding_bricks)
for i in range(no_of_breakable_bricks):
    brick_arr[i] = Breakable(str(i))

# brick_arr[0].x = 3
# brick_arr[0].y = 7

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

for i in range(no_of_unbreakable_bricks):
    brick_arr[no_of_breakable_bricks + i] = Unbreakable(no_of_breakable_bricks+i)
    brick_arr[no_of_breakable_bricks + i].strength = 1000

for i in range(no_of_exploding_bricks):
    brick_arr[no_of_breakable_bricks + no_of_unbreakable_bricks + i] = Exploding(no_of_breakable_bricks + no_of_unbreakable_bricks + i)

brick_arr[8].x = 3
brick_arr[8].y = 4
brick_arr[9].x = 7
brick_arr[9].y = 5
brick_arr[10].x = 11
brick_arr[10].y = 3
brick_arr[0].x = 15
brick_arr[0].y = 3

# populate bricks
# change brick ball collision to make sesk
# get code out of main? move shit to config?
# fix edge collision for paddle maybe

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

        for i in range(no_of_breakable_bricks + no_of_unbreakable_bricks + no_of_exploding_bricks):
            brick_arr[i].disp(screen)
        newPaddle.disp(screen)

        if(ball_move == 1):
            newBall.paddle_collison(screen, newPaddle)
            

        newBall.brick_collision(screen, brick_arr)

        i = 0

        while (i < len(config.falling_powerups)):
            if(config.falling_powerups[i].move()):
                config.falling_powerups[i].disp(screen)
                config.falling_powerups[i].caught(screen)
                i += 1
        i = 0
        while (i < len(config.active_powerups)):
            flag = 0
            if(time_played - config.active_powerups[i].time > 20):
                if(config.active_powerups[i].which == 1):
                    newPaddle.length -= 2
                if(config.active_powerups[i].which == 2):
                    newPaddle.length += 2
                if(config.active_powerups[i].which == 3):
                    newPaddle.length += 2
                if(config.active_powerups[i].which == 4):
                    if(newBall.x_vel > 0):
                            newBall.x_vel -= 1
                    if(newBall.x_vel < 0):
                            newBall.x_vel += 1
                if(config.active_powerups[i].which == 5):
                    newPaddle.length += 2
                if(config.active_powerups[i].which == 6):
                    newPaddle.length += 2
                config.active_powerups.remove(config.active_powerups[i])
                i -= 1
                flag = 1
            if(flag == 0):
                if(config.active_powerups[i].which == 1 and config.active_powerups[i].active == 0):
                    newPaddle.length += 2
                    config.active_powerups[i].active = 1
                if(config.active_powerups[i].which == 2 and config.active_powerups[i].active == 0):
                    newPaddle.length -= 2
                    config.active_powerups[i].active = 1
                if(config.active_powerups[i].which == 3 and config.active_powerups[i].active == 0):
                    newPaddle.length -= 2
                    config.active_powerups[i].active = 1
                if(config.active_powerups[i].which == 4 and config.active_powerups[i].active == 0):
                    if(newBall.x_vel > 0):
                        newBall.x_vel += 1
                    if(newBall.x_vel < 0):
                        newBall.x_vel -= 1
                    config.active_powerups[i].active = 1
                if(config.active_powerups[i].which == 5 and config.active_powerups[i].active == 0):
                    newPaddle.length -= 2
                    config.active_powerups[i].active = 1
                if(config.active_powerups[i].which == 6 and config.active_powerups[i].active == 0):
                    newPaddle.length -= 2
                    config.active_powerups[i].active = 1
            i += 1
        newBall.disp(screen)

        if(newBall.y == rows+1):
            lives -= 1
            break
        # print(newBall.x_vel)

        print('\033[0;0H')
        # print("\033[H\033[J")

        for i in screen:
            for j in i:
                if(j == '0' or j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9' or j == '10' or j == '11' or j == '12' or j == '13' or j == '14' or j == '15' or j == '16'):
                    curr = int(j)
                    if(brick_arr[curr].strength == 69):
                        print(Fore.MAGENTA + Back.MAGENTA, end="")
                        print(' ', end="")
                        print(Style.RESET_ALL, end="")
                    elif(brick_arr[curr].strength > 3):
                        print(Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX, end="")
                        print(' ', end="")
                        print(Style.RESET_ALL, end="")
                    elif(brick_arr[curr].strength == 3):
                        print(Fore.RED + Back.RED, end="")
                        print(' ', end="")
                        print(Style.RESET_ALL, end="")
                    elif(brick_arr[curr].strength == 2):
                        print(Fore.YELLOW + Back.YELLOW, end="")
                        print(' ', end="")
                        print(Style.RESET_ALL, end="")
                    elif(brick_arr[curr].strength == 1):
                        print(Fore.GREEN + Back.GREEN, end="")
                        print(' ', end="")
                        print(Style.RESET_ALL, end="")
                    elif(brick_arr[curr].strength == 0):
                        print(' ', end="")
                else:
                    print(j, end="")

        print("LIVES: ", lives)
        print("TIME:  ", round(time_played - initial_time))
        print("SCORE: ", config.score)
        power_up_print = ""
        for i in range (len(config.active_powerups)):
            if(config.active_powerups[i].which == 1):
                power_up_print += "ep  "
            if(config.active_powerups[i].which == 2):
                power_up_print += "sp  "
            if(config.active_powerups[i].which == 3):
                power_up_print += "bm  "
            if(config.active_powerups[i].which == 4):
                power_up_print += "fb  "
            if(config.active_powerups[i].which == 5):
                power_up_print += "tb  "
            if(config.active_powerups[i].which == 6):
                power_up_print += "pg  "
        print('\033[0K', end='')
        print("ACTIVE POWER UPS: ", power_up_print)

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
        
        broken = 0
        for i in range (no_of_breakable_bricks):
            if(brick_arr[i].strength == 0):
                broken+=1
        for i in range (no_of_exploding_bricks):
            if(brick_arr[no_of_breakable_bricks+no_of_unbreakable_bricks].strength == 0):
                broken+=1
        if(broken == no_of_breakable_bricks+no_of_exploding_bricks):
            # config.score += lives*20
            print("WOW BHAIYA")
            system("stty echo")
            quit()

    config.no_of_falling_powerups = 0
    config.no_of_active_powerups = 0
    config.active_powerups.clear()
    config.falling_powerups.clear()

print("GAME OVER")

# except:
system("stty echo")