import colorama
from input import input_to, Get
from os import system
import numpy as np
from time import sleep
from colorama import Back, Fore, Style
from paddles import Paddle
from bricks import Unbreakable, Breakable, Exploding, Rainbow, BossBrick
from balls import Ball
from bullets import Bullet
from boss import Boss
from bombs import Bomb
import time
import config
import sounds

# try:
rows = 40
columns = 80
paddle_char = '='
ball_char = 'O'
brick_length = 4
no_of_breakable_bricks = 20
no_of_unbreakable_bricks = 10
no_of_exploding_bricks = 12
no_of_rainbow_bricks = 1
no_of_total_bricks = no_of_breakable_bricks + no_of_unbreakable_bricks + no_of_exploding_bricks + no_of_rainbow_bricks
lives = 3
ball_speed = 3
initial_time = time.time()
left_border = '⎹'
right_border = '⎸'
bottom_border = '‾'
top_border = '_'
system("stty -echo")
next_level = 0
brick_arr1 = [0]*(no_of_total_bricks)
for i in range(no_of_breakable_bricks):
    brick_arr1[i] = Breakable(str(i))

for i in range(no_of_unbreakable_bricks):
    brick_arr1[no_of_breakable_bricks + i] = Unbreakable(no_of_breakable_bricks+i)
    brick_arr1[no_of_breakable_bricks + i].strength = 1000

for i in range(no_of_exploding_bricks):
    brick_arr1[no_of_breakable_bricks + no_of_unbreakable_bricks + i] = Exploding(no_of_breakable_bricks + no_of_unbreakable_bricks + i)

for i in range(no_of_rainbow_bricks):
    brick_arr1[no_of_breakable_bricks + no_of_unbreakable_bricks + no_of_exploding_bricks + i] = Rainbow(no_of_breakable_bricks + no_of_unbreakable_bricks + no_of_exploding_bricks + i)

brick_arr1[0].x = np.random.randint(3, 7)
brick_arr1[0].y = np.random.randint(3, 9)
brick_arr1[1].x = np.random.randint(11, 15)
brick_arr1[1].y = np.random.randint(3, 9)
brick_arr1[2].x = np.random.randint(59, 63)
brick_arr1[2].y = np.random.randint(3, 9)
brick_arr1[3].x = np.random.randint(27, 31)
brick_arr1[3].y = np.random.randint(3, 9)
brick_arr1[4].x = np.random.randint(35, 39)
brick_arr1[4].y = np.random.randint(3, 9)
brick_arr1[5].x = np.random.randint(43, 47)
brick_arr1[5].y = np.random.randint(3, 9)

brick_arr1[20].x = np.random.randint(51, 55)
brick_arr1[20].y = np.random.randint(3, 9)
brick_arr1[21].x = np.random.randint(19, 23)
brick_arr1[21].y = np.random.randint(3, 9)
brick_arr1[22].x = np.random.randint(67, 71)
brick_arr1[22].y = np.random.randint(3, 9)
brick_arr1[23].x = np.random.randint(75, 76)
brick_arr1[23].y = np.random.randint(3, 9)

randi = np.random.randint(1,3)

brick_arr1[26].x = np.random.randint(3,6)
brick_arr1[26].y = np.random.randint(15,17)
brick_arr1[7].x = np.random.randint(11,13)
brick_arr1[7].y = np.random.randint(15,17)
brick_arr1[25].x = np.random.randint(17,19)
brick_arr1[25].y = np.random.randint(15,17)
brick_arr1[6].x = np.random.randint(23,25)
brick_arr1[6].y = np.random.randint(15,17)
brick_arr1[27].x = np.random.randint(29,31)
brick_arr1[27].y = np.random.randint(15,17)
brick_arr1[28].x = np.random.randint(35,37)
brick_arr1[28].y = np.random.randint(15,17)

brick_arr1[30].x = 5 + randi
brick_arr1[30].y = 20 + randi
brick_arr1[31].x = 9 + randi
brick_arr1[31].y = 22 + randi
brick_arr1[32].x = 13 + randi
brick_arr1[32].y = 23 + randi
brick_arr1[33].x = 17 + randi
brick_arr1[33].y = 24 + randi
brick_arr1[34].x = 21 + randi
brick_arr1[34].y = 22 + randi
brick_arr1[35].x = 25 + randi
brick_arr1[35].y = 21 + randi

brick_arr1[12].x = 5 + randi
brick_arr1[12].y = 24 + randi
brick_arr1[13].x = 9 + randi
brick_arr1[13].y = 26 + randi
brick_arr1[14].x = 13 + randi
brick_arr1[14].y = 27 + randi
brick_arr1[15].x = 17 + randi
brick_arr1[15].y = 28 + randi
brick_arr1[16].x = 21 + randi
brick_arr1[16].y = 26 + randi
brick_arr1[17].x = 25 + randi
brick_arr1[17].y = 25 + randi

brick_arr1[24].x = 29 + randi
brick_arr1[24].y = 21 + randi

randi = np.random.randint(1,6)
yrandi = np.random.randint(1,10)

brick_arr1[36].x = 50 + randi
brick_arr1[36].y = 12 + yrandi
brick_arr1[37].x = 54 + randi
brick_arr1[37].y = 14 + yrandi
brick_arr1[38].x = 58 + randi
brick_arr1[38].y = 15 + yrandi
brick_arr1[39].x = 62 + randi
brick_arr1[39].y = 16 + yrandi
brick_arr1[40].x = 66 + randi
brick_arr1[40].y = 14 + yrandi
brick_arr1[41].x = 70 + randi
brick_arr1[41].y = 13 + yrandi

brick_arr1[18].x = 50 + randi
brick_arr1[18].y = 16 + yrandi
brick_arr1[19].x = 54 + randi
brick_arr1[19].y = 18 + yrandi
brick_arr1[8].x = 58 + randi
brick_arr1[8].y = 19 + yrandi
brick_arr1[9].x = 62 + randi
brick_arr1[9].y = 20 + yrandi
brick_arr1[10].x = 66 + randi
brick_arr1[10].y = 18 + yrandi
brick_arr1[11].x = 70 + randi
brick_arr1[11].y = 17 + yrandi

brick_arr1[29].x = 46 + randi
brick_arr1[29].y = 12 + yrandi

brick_arr1[42].x = 40
brick_arr1[42].y = 20

brick_arr2 = [0]*(25)
for i in range(20):
    brick_arr2[i] = Breakable(str(i))
for i in range(5):
    brick_arr2[i+20] = Rainbow(str(i+20))

brick_arr2[0].x = 5
brick_arr2[0].y = 5
brick_arr2[1].x = 10
brick_arr2[1].y = 10
brick_arr2[2].x = 20
brick_arr2[2].y = 20
brick_arr2[3].x = 50
brick_arr2[3].y = 20
brick_arr2[4].x = 60
brick_arr2[4].y = 5
brick_arr2[5].x = 5
brick_arr2[5].y = 10
brick_arr2[6].x = 15
brick_arr2[6].y = 10
brick_arr2[7].x = 25
brick_arr2[7].y = 20
brick_arr2[8].x = 40
brick_arr2[8].y = 20
brick_arr2[9].x = 10
brick_arr2[9].y = 14
brick_arr2[10].x = 5
brick_arr2[10].y = 25
brick_arr2[11].x = 15
brick_arr2[11].y = 25
brick_arr2[12].x = 25
brick_arr2[12].y = 25
brick_arr2[13].x = 40
brick_arr2[13].y = 25
brick_arr2[14].x = 60
brick_arr2[14].y = 25
brick_arr2[15].x = 38
brick_arr2[15].y = 29
brick_arr2[16].x = 42
brick_arr2[16].y = 29
brick_arr2[17].x = 46
brick_arr2[17].y = 29
brick_arr2[18].x = 50
brick_arr2[18].y = 29
brick_arr2[19].x = 54
brick_arr2[19].y = 29
brick_arr2[20].x = 70
brick_arr2[20].y = 10
brick_arr2[21].x = 70
brick_arr2[21].y = 16
brick_arr2[22].x = 70
brick_arr2[22].y = 22
brick_arr2[23].x = 70
brick_arr2[23].y = 4
brick_arr2[24].x = 70
brick_arr2[24].y = 29

brick_arr3 = [0]*(5)
for i in range(5):
    brick_arr3[i] = Unbreakable(str(i))
brick_arr3[0].x = 5
brick_arr3[0].y = 20
brick_arr3[1].x = 10
brick_arr3[1].y = 25
brick_arr3[2].x = 32
brick_arr3[2].y = 24
brick_arr3[3].x = 50
brick_arr3[3].y = 20
brick_arr3[4].x = 70
brick_arr3[4].y = 22

# change brick ball collision to make sesk
# get code out of main? move shit to config?
# paddle ball overlapping sometimes after wall collision
# multiple through ball powerups simultaneously once first ends second stops working (through_ball var)
# random errors with rainbow fireball

for l in range (3):
    config.bullets.clear()
    brick_arr = []
    if(l == 0):
        # no_of_breakable_bricks = 20
        # no_of_unbreakable_bricks = 0
        # no_of_exploding_bricks = 0
        # no_of_rainbow_bricks = 5
        # no_of_total_bricks = no_of_breakable_bricks + no_of_unbreakable_bricks + no_of_exploding_bricks + no_of_rainbow_bricks
        brick_arr = brick_arr1
    if(l == 1):
        no_of_breakable_bricks = 20
        no_of_unbreakable_bricks = 0
        no_of_exploding_bricks = 0
        no_of_rainbow_bricks = 5
        no_of_total_bricks = no_of_breakable_bricks + no_of_unbreakable_bricks + no_of_exploding_bricks + no_of_rainbow_bricks
        brick_arr = brick_arr2

    elif(l == 2):
        no_of_breakable_bricks = 0
        no_of_unbreakable_bricks = 5
        no_of_exploding_bricks = 0
        no_of_rainbow_bricks = 0
        no_of_total_bricks = no_of_breakable_bricks + no_of_unbreakable_bricks + no_of_exploding_bricks + no_of_rainbow_bricks
        brick_arr = brick_arr3
        newBoss = Boss(newPaddle)

    while True:
        newPaddle = Paddle(7)
        newBall = Ball(newPaddle)
        ball_move = 0
        ticks = 3
        through_ball = 0
        starting_life_time = time.time()
        current_life_time = 0
        config.paddle_shooter = 0
        config.bullets.clear()
        hit = 0
        if(next_level == 1):
            next_level = 0
            break
        while True:
            if(next_level == 1):
                break
            current_life_time = time.time()
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

            for i in range(len(brick_arr)):
                if(brick_arr[i].strength>0):
                    brick_arr[i].disp(screen)
            newPaddle.disp(screen)
            if(l == 2):
                if(ticks%45 == 0):
                    sounds.play_sound2()
                newBoss.move(newPaddle)
                newBoss.disp(screen)
                newBall.boss_collision(screen, newBoss)
                if(newBoss.health == 0):
                    print("\nWOW BHAIYA")
                    system("stty echo")
                    quit()
                if(newBoss.health == 6 and newBoss.defense1 == 0):
                    newBoss.defense1 = 1
                    for i in range(19):
                        brick_arr.append(BossBrick(str(no_of_total_bricks + i)))
                        brick_arr[no_of_total_bricks+i].y = 10
                        brick_arr[no_of_total_bricks+i].x = 4*i + 4
                    no_of_total_bricks+=19
                if(newBoss.health == 3 and newBoss.defense2 == 0):
                    newBoss.defense2 = 1
                    for i in range(19):
                        brick_arr.append(BossBrick(str(no_of_total_bricks + i)))
                        brick_arr[no_of_total_bricks+i].y = 5
                        brick_arr[no_of_total_bricks+i].x = 4*i + 4
                    no_of_total_bricks+=19

                    i = 0

                if(lives == 0):
                    print("\nGAME OVER")
                    system("stty echo")
                    quit()

                i = 0

                if(ticks%100 == 0):
                    config.bombs.append(Bomb(newBoss))
                while i < len(config.bombs):
                    if(config.bombs[i].hit(screen)):
                        hit = 1
                        lives -= 1
                        break
                    config.bombs[i].move()
                    config.bombs[i].disp(screen)
                    i += 1

                
                if(hit == 1):
                    config.bombs.clear()
                    hit = 0
                    break
            
            
            i = 0


            if(ball_move == 1):
                newBall.paddle_collison(screen, newPaddle, round(current_life_time - starting_life_time), brick_arr, no_of_total_bricks, ticks)
                
            if(through_ball == 0):
                newBall.brick_collision(screen, brick_arr)
                for i in range(no_of_rainbow_bricks):
                    if(brick_arr[no_of_breakable_bricks+no_of_unbreakable_bricks+no_of_exploding_bricks+i].collided == 0):
                        brick_arr[no_of_breakable_bricks+no_of_unbreakable_bricks+no_of_exploding_bricks+i].changeStrength(no_of_breakable_bricks+no_of_unbreakable_bricks+no_of_exploding_bricks+i)

            else:
                newBall.brick_destroy(screen, brick_arr)
            
            i = 0

            if(config.paddle_shooter == 1):
                if(ticks%15 == 0):
                    sounds.play_sound()
                    config.bullets.append(Bullet(newPaddle.x))
                    config.bullets.append(Bullet(newPaddle.x + newPaddle.length))
                while (i < len(config.bullets)):
                    config.bullets[i].move()
                    config.bullets[i].disp(screen)
                    config.bullets[i].collision(screen, brick_arr)
                    i += 1

            i = 0

            for i in range(no_of_total_bricks):
                if(brick_arr[i].y == 37 and brick_arr[i].strength > 0):
                        system("stty echo")
                        quit()


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
                        config.fire_ball = False
                        config.bullets.clear()
                    if(config.active_powerups[i].which == 4):
                        if(newBall.x_vel > 0):
                                newBall.x_vel -= 1
                        if(newBall.x_vel < 0):
                                newBall.x_vel += 1
                    if(config.active_powerups[i].which == 5):
                        through_ball = 0
                    if(config.active_powerups[i].which == 6):
                        config.paddle_shooter = 0
                        config.bullets.clear()
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
                        config.fire_ball = True
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
                        config.paddle_shooter = 1
                        config.active_powerups[i].active = 1
                i += 1
            newBall.disp(screen)

            if(newBall.y == rows+1):
                lives -= 1
                if(lives == 0):
                    print("GAME OVER")
                    system("stty echo")
                    quit()
                # next_level = 0
                break
            # print(newBall.x_vel)

            print('\033[0;0H')
            # print("\033[H\033[J")

            brick_dup = brick_arr.copy()

            brick_dup.sort(key=lambda x: x.strength)

            for i in screen:
                for j in i:
                    if(j == '0' or j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9' or j == '10' or j == '11' or j == '12' or j == '13' or j == '14' or j == '15' or j == '16' or j == '17' or j == '18' or j == '19' or j == '20' or j == '21' or j == '22' or j == '23' or j == '24' or j == '25' or j == '26' or j == '27' or j == '28' or j == '29' or j == '30' or j == '31' or j == '32' or j == '33' or j == '34' or j == '35' or j == '36' or j == '37' or j == '38' or j == '39' or j == '40' or j == '41' or j == '42' or j == '43' or j == '44' or j == '45'):
                        curr = int(j)
                        if(curr < len(brick_arr)):
                            if(brick_arr[curr].strength == 0):
                                print(' ', end="")
                            if(brick_arr[curr].strength == 69):
                                print(Fore.MAGENTA + Back.MAGENTA, end="")
                                print(' ', end="")
                                print(Style.RESET_ALL, end="")
                            elif(brick_arr[curr].strength > 3):
                                print(Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX, end="")
                                print(' ', end="")
                                print(Style.RESET_ALL, end="")
                            elif(brick_arr[curr].strength == 3):
                                print(Fore.WHITE + Back.RED, end="")
                                print(' ', end="")
                                print(Style.RESET_ALL, end="")
                            elif(brick_arr[curr].strength == 2):
                                print(Fore.WHITE + Back.YELLOW, end="")
                                print(' ', end="")
                                print(Style.RESET_ALL, end="")
                            elif(brick_arr[curr].strength == 1):
                                print(Fore.WHITE + Back.GREEN, end="")
                                print(' ', end="")
                                print(Style.RESET_ALL, end="")

                    else:
                        if(config.paddle_shooter == 1 and j == paddle_char):
                            print(Fore.MAGENTA + Back.MAGENTA, end="")
                            print(j, end="")
                            print(Style.RESET_ALL, end="")
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
                    power_up_print += "fi  "
                if(config.active_powerups[i].which == 4):
                    power_up_print += "fb  "
                if(config.active_powerups[i].which == 5):
                    power_up_print += "tb  "
                if(config.active_powerups[i].which == 6):
                    power_up_print += "sh  "
            print('\033[0K', end='')
            print("ACTIVE POWER UPS: ", power_up_print)
            if(l == 2):
                print("BOSS HEALTH: ", end = '')
                for i in range (9):
                    if(i<newBoss.health):
                        print('#', end = '')
                    else:
                        print(' ', end = '')
                # print('\n')

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
            
            if(key == "c"):
                next_level = 1
                break
            
            broken = 0
            for i in range (no_of_breakable_bricks):
                if(brick_arr[i].strength == 0):
                    broken+=1
            for i in range (no_of_exploding_bricks):
                if(brick_arr[no_of_breakable_bricks+no_of_unbreakable_bricks + i].strength == 0):
                    broken+=1
            for i in range(no_of_rainbow_bricks):
                if(brick_arr[no_of_breakable_bricks+no_of_unbreakable_bricks+no_of_exploding_bricks + i].strength == 0):
                    broken+=1
            if(broken == no_of_breakable_bricks+no_of_exploding_bricks+no_of_rainbow_bricks):
                if(l != 2):
                    next_level = 1
                    break

        config.no_of_falling_powerups = 0
        config.no_of_active_powerups = 0
        config.active_powerups.clear()
        config.falling_powerups.clear()
        config.bombs.clear()

# print("WOW BHAIYA")
# system("stty echo")
# quit()    

print("\nGAME OVER")

# except:
system("stty echo")