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
rows = 40
columns = 80
paddle_char = '='
ball_char = 'O'
brick_length = 4
no_of_breakable_bricks = 20
no_of_unbreakable_bricks = 10
no_of_exploding_bricks = 12
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

for i in range(no_of_unbreakable_bricks):
    brick_arr[no_of_breakable_bricks + i] = Unbreakable(no_of_breakable_bricks+i)
    brick_arr[no_of_breakable_bricks + i].strength = 1000

for i in range(no_of_exploding_bricks):
    brick_arr[no_of_breakable_bricks + no_of_unbreakable_bricks + i] = Exploding(no_of_breakable_bricks + no_of_unbreakable_bricks + i)

brick_arr[0].x = np.random.randint(3, 7)
brick_arr[0].y = np.random.randint(3, 9)
brick_arr[1].x = np.random.randint(11, 15)
brick_arr[1].y = np.random.randint(3, 9)
brick_arr[2].x = np.random.randint(59, 63)
brick_arr[2].y = np.random.randint(3, 9)
brick_arr[3].x = np.random.randint(27, 31)
brick_arr[3].y = np.random.randint(3, 9)
brick_arr[4].x = np.random.randint(35, 39)
brick_arr[4].y = np.random.randint(3, 9)
brick_arr[5].x = np.random.randint(43, 47)
brick_arr[5].y = np.random.randint(3, 9)

brick_arr[20].x = np.random.randint(51, 55)
brick_arr[20].y = np.random.randint(3, 9)
brick_arr[21].x = np.random.randint(19, 23)
brick_arr[21].y = np.random.randint(3, 9)
brick_arr[22].x = np.random.randint(67, 71)
brick_arr[22].y = np.random.randint(3, 9)
brick_arr[23].x = np.random.randint(75, 76)
brick_arr[23].y = np.random.randint(3, 9)

randi = np.random.randint(1,3)

brick_arr[26].x = np.random.randint(3,6)
brick_arr[26].y = np.random.randint(15,17)
brick_arr[7].x = np.random.randint(11,13)
brick_arr[7].y = np.random.randint(15,17)
brick_arr[25].x = np.random.randint(17,19)
brick_arr[25].y = np.random.randint(15,17)
brick_arr[6].x = np.random.randint(23,25)
brick_arr[6].y = np.random.randint(15,17)
brick_arr[27].x = np.random.randint(29,31)
brick_arr[27].y = np.random.randint(15,17)
brick_arr[28].x = np.random.randint(35,37)
brick_arr[28].y = np.random.randint(15,17)

brick_arr[30].x = 5 + randi
brick_arr[30].y = 20 + randi
brick_arr[31].x = 9 + randi
brick_arr[31].y = 22 + randi
brick_arr[32].x = 13 + randi
brick_arr[32].y = 23 + randi
brick_arr[33].x = 17 + randi
brick_arr[33].y = 24 + randi
brick_arr[34].x = 21 + randi
brick_arr[34].y = 22 + randi
brick_arr[35].x = 25 + randi
brick_arr[35].y = 21 + randi

brick_arr[12].x = 5 + randi
brick_arr[12].y = 24 + randi
brick_arr[13].x = 9 + randi
brick_arr[13].y = 26 + randi
brick_arr[14].x = 13 + randi
brick_arr[14].y = 27 + randi
brick_arr[15].x = 17 + randi
brick_arr[15].y = 28 + randi
brick_arr[16].x = 21 + randi
brick_arr[16].y = 26 + randi
brick_arr[17].x = 25 + randi
brick_arr[17].y = 25 + randi

brick_arr[24].x = 29 + randi
brick_arr[24].y = 21 + randi

randi = np.random.randint(1,6)
yrandi = np.random.randint(1,10)

brick_arr[36].x = 50 + randi
brick_arr[36].y = 12 + yrandi
brick_arr[37].x = 54 + randi
brick_arr[37].y = 14 + yrandi
brick_arr[38].x = 58 + randi
brick_arr[38].y = 15 + yrandi
brick_arr[39].x = 62 + randi
brick_arr[39].y = 16 + yrandi
brick_arr[40].x = 66 + randi
brick_arr[40].y = 14 + yrandi
brick_arr[41].x = 70 + randi
brick_arr[41].y = 13 + yrandi

brick_arr[18].x = 50 + randi
brick_arr[18].y = 16 + yrandi
brick_arr[19].x = 54 + randi
brick_arr[19].y = 18 + yrandi
brick_arr[8].x = 58 + randi
brick_arr[8].y = 19 + yrandi
brick_arr[9].x = 62 + randi
brick_arr[9].y = 20 + yrandi
brick_arr[10].x = 66 + randi
brick_arr[10].y = 18 + yrandi
brick_arr[11].x = 70 + randi
brick_arr[11].y = 17 + yrandi

brick_arr[29].x = 46 + randi
brick_arr[29].y = 12 + yrandi

# change brick ball collision to make sesk
# get code out of main? move shit to config?
# paddle ball overlapping sometimes after wall collision
# multiple through ball powerups simultaneously once first ends second stops working

for k in range(3):
    newPaddle = Paddle(7)
    newBall = Ball(newPaddle)
    ball_move = 0
    ticks = 3
    through_ball = 0

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
            
        if(through_ball == 0):
            newBall.brick_collision(screen, brick_arr)
        else:
            newBall.brick_destroy(screen, brick_arr)

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
                    through_ball = 0
                if(config.active_powerups[i].which == 4):
                    if(newBall.x_vel > 0):
                            newBall.x_vel -= 1
                    if(newBall.x_vel < 0):
                            newBall.x_vel += 1
                if(config.active_powerups[i].which == 5):
                    through_ball = 0
                if(config.active_powerups[i].which == 6):
                    through_ball = 0
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
                    through_ball = 1
                    config.active_powerups[i].active = 1
                if(config.active_powerups[i].which == 4 and config.active_powerups[i].active == 0):
                    if(newBall.x_vel > 0):
                        newBall.x_vel += 1
                    if(newBall.x_vel < 0):
                        newBall.x_vel -= 1
                    config.active_powerups[i].active = 1
                if(config.active_powerups[i].which == 5 and config.active_powerups[i].active == 0):
                    through_ball = 1
                    config.active_powerups[i].active = 1
                if(config.active_powerups[i].which == 6 and config.active_powerups[i].active == 0):
                    through_ball = 1
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
                if(j == '0' or j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9' or j == '10' or j == '11' or j == '12' or j == '13' or j == '14' or j == '15' or j == '16' or j == '17' or j == '18' or j == '19' or j == '20' or j == '21' or j == '22' or j == '23' or j == '24' or j == '25' or j == '26' or j == '27' or j == '28' or j == '29' or j == '30' or j == '31' or j == '32' or j == '33' or j == '34' or j == '35' or j == '36' or j == '37' or j == '38' or j == '39' or j == '40' or j == '41' or j == '42' or j == '43' or j == '44' or j == '45'):
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
            if(brick_arr[no_of_breakable_bricks+no_of_unbreakable_bricks + i].strength == 0):
                broken+=1
        # print(broken)
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