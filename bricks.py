import numpy as np
import config
from powerups import ExpandPaddle, ShrinkPaddle, FireBall, FastBall, ThroughBall, ShootingPaddle

rows = 40
columns = 80
paddle_char = '='
ball_char = 'O'
brick_length = 4
lives = 3
no_of_breakable_bricks = 6
no_of_unbreakable_bricks = 2
no_of_exploding_bricks = 4
bullet_char = '.'


class Brick:
    def __init__(self, index):
        self.x = 0
        self.y = 0
        self.index = index

    def disp(self, arr):
        for i in range(brick_length):
            for j in range(brick_length):
                if(self.strength == 0):
                    arr[self.y + j][self.x + i] = ' '
                else:
                    arr[self.y + j][self.x + i] = str(self.index)
    
    def falling(self):
        if(self.strength>0):
            self.y += 1

    def collision(self, arr, Brick_arr, ball_velocities):
        if (self.strength > 0):
            if(self.strength == 1):
                rand = np.random.randint(1, 4)
                # rand = 3
                if(rand % 3 == 0):
                    rand2 = np.random.randint(1, 7)
                    if(rand2 == 1):
                        config.falling_powerups.append(ExpandPaddle(self.x, self.y, ball_velocities))
                    if(rand2 == 2):
                        config.falling_powerups.append(ShrinkPaddle(self.x, self.y, ball_velocities))
                    if(rand2 == 3):
                        config.falling_powerups.append(FireBall(self.x, self.y, ball_velocities))
                    if(rand2 == 4):
                        config.falling_powerups.append(FastBall(self.x, self.y, ball_velocities))
                    if(rand2 == 5):
                        config.falling_powerups.append(
                            ThroughBall(self.x, self.y, ball_velocities))
                    if(rand2 == 6):
                        config.falling_powerups.append(ShootingPaddle(self.x, self.y, ball_velocities))
                config.score += 10
            self.strength -= 1

    def destroy(self, arr, Brick_arr, ball_velocities):
        self.collision(arr, Brick_arr, ball_velocities)
        if(self.strength > 0):
            rand = np.random.randint(1, 4)
            # rand = 3
            if(rand % 3 == 0):
                rand2 = np.random.randint(1, 7)
                if(rand2 == 1):
                    config.falling_powerups.append(
                        ExpandPaddle(self.x, self.y, ball_velocities))
                if(rand2 == 2):
                    config.falling_powerups.append(
                        ShrinkPaddle(self.x, self.y, ball_velocities))
                if(rand2 == 3):
                    config.falling_powerups.append(FireBall(self.x, self.y, ball_velocities))
                if(rand2 == 4):
                    config.falling_powerups.append(FastBall(self.x, self.y, ball_velocities))
                if(rand2 == 5):
                    config.falling_powerups.append(ThroughBall(self.x, self.y, ball_velocities))
                if(rand2 == 6):
                    config.falling_powerups.append(ShootingPaddle(self.x, self.y, ball_velocities))
            self.strength = 0
            config.score += 10
            for i in range(brick_length):
                for j in range(brick_length):
                    arr[self.y + j][self.x + i] = ' '
    
    def explode(self, arr, Brick_arr, ball_velocities):
        if(self.strength > 0):
            rand = np.random.randint(1, 4)
            # rand = 3
            if(rand % 3 == 0):
                rand2 = np.random.randint(1, 7)
                if(rand2 == 1):
                    config.falling_powerups.append(
                        ExpandPaddle(self.x, self.y, ball_velocities))
                if(rand2 == 2):
                    config.falling_powerups.append(
                        ShrinkPaddle(self.x, self.y, ball_velocities))
                if(rand2 == 3):
                    config.falling_powerups.append(FireBall(self.x, self.y, ball_velocities))
                if(rand2 == 4):
                    config.falling_powerups.append(FastBall(self.x, self.y, ball_velocities))
                if(rand2 == 5):
                    config.falling_powerups.append(ThroughBall(self.x, self.y, ball_velocities))
                if(rand2 == 6):
                    config.falling_powerups.append(ShootingPaddle(self.x, self.y, ball_velocities))
        self.strength = 0
        config.score += 10
        for i in range(brick_length):
            for j in range(brick_length):
                arr[self.y + j][self.x + i] = ' '

        if((arr[self.y-1][self.x] != ' ') and (arr[self.y-1][self.x] != ball_char) and (arr[self.y-1][self.x] != bullet_char)):
            curr = int(arr[self.y-1][self.x])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y][self.x-1] != ' ') and (arr[self.y][self.x-1] != ball_char) and (arr[self.y][self.x-1] != bullet_char)):
            curr = int(arr[self.y][self.x-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y+brick_length][self.x] != ' ') and (arr[self.y+brick_length][self.x] != ball_char) and (arr[self.y+brick_length][self.x] != bullet_char)):
            curr = int(arr[self.y+brick_length][self.x])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y+brick_length-1][self.x-1] != ' ') and (arr[self.y+brick_length-1][self.x-1] != ball_char) and (arr[self.y+brick_length-1][self.x-1] != bullet_char)):
            curr = int(arr[self.y+brick_length-1][self.x-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y][self.x+brick_length] != ' ') and (arr[self.y][self.x+brick_length] != ball_char) and (arr[self.y][self.x+brick_length] != bullet_char)):
            curr = int(arr[self.y][self.x+brick_length])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y-1][self.x+brick_length-1] != ' ') and (arr[self.y-1][self.x+brick_length-1] != ball_char) and (arr[self.y-1][self.x+brick_length-1] != bullet_char)):
            curr = int(arr[self.y-1][self.x+brick_length-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y+brick_length][self.x+brick_length-1] != ' ') and (arr[self.y+brick_length][self.x+brick_length-1] != ball_char) and (arr[self.y+brick_length][self.x+brick_length-1] != bullet_char)):
            curr = int(arr[self.y+brick_length][self.x+brick_length-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y+brick_length-1][self.x+brick_length] != ' ') and (arr[self.y+brick_length-1][self.x+brick_length] != ball_char) and (arr[self.y+brick_length-1][self.x+brick_length] != bullet_char)):
            curr = int(arr[self.y+brick_length-1][self.x+brick_length])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y-1][self.x-1] != ' ') and (arr[self.y-1][self.x-1] != ball_char) and (arr[self.y-1][self.x-1] != bullet_char)):
            curr = int(arr[self.y-1][self.x-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y-1][self.x+brick_length] != ' ') and (arr[self.y-1][self.x+brick_length] != ball_char) and (arr[self.y-1][self.x+brick_length] != bullet_char)):
            curr = int(arr[self.y-1][self.x+brick_length])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y+brick_length][self.x-1] != ' ') and (arr[self.y+brick_length][self.x-1] != ball_char) and (arr[self.y+brick_length][self.x-1] != bullet_char)):
            curr = int(arr[self.y+brick_length][self.x-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y+brick_length][self.x+brick_length] != ' ') and (arr[self.y+brick_length][self.x+brick_length] != ball_char) and (arr[self.y+brick_length][self.x+brick_length] != bullet_char)):
            curr = int(arr[self.y+brick_length][self.x+brick_length])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)


class Unbreakable(Brick):
    pass

    def __init__(self, index):
        self.strength = 100000
        super().__init__(index)


class Breakable(Brick):
    pass

    def __init__(self, index):
        self.strength = np.random.randint(1, 4)
        super().__init__(index)


class Rainbow(Brick):
    pass

    def __init__(self, index):
        self.strength = np.random.randint(1, 4)
        super().__init__(index)
        self.collided = 0

    def changeStrength(self, index):
        self.strength = np.random.randint(1, 4)

    def collision(self, arr, Brick_arr, ball_velocities):
        self.collided = 1
        if (self.strength > 0):
            if(self.strength == 1):
                rand = np.random.randint(1, 4)
                # rand = 3
                if(rand % 3 == 0):
                    rand2 = np.random.randint(1, 7)
                    if(rand2 == 1):
                        config.falling_powerups.append(
                            ExpandPaddle(self.x, self.y, ball_velocities))
                    if(rand2 == 2):
                        config.falling_powerups.append(
                            ShrinkPaddle(self.x, self.y, ball_velocities))
                    if(rand2 == 3):
                        config.falling_powerups.append(FireBall(self.x, self.y, ball_velocities))
                    if(rand2 == 4):
                        config.falling_powerups.append(
                            FastBall(self.x, self.y, ball_velocities))
                    if(rand2 == 5):
                        config.falling_powerups.append(
                            ThroughBall(self.x, self.y, ball_velocities))
                    if(rand2 == 6):
                        config.falling_powerups.append(ShootingPaddle(self.x, self.y, ball_velocities))
                config.score += 10
            self.strength -= 1


class Exploding(Brick):
    pass

    def __init__(self, index):
        self.strength = 69
        super().__init__(index)

    def collision(self, arr, Brick_arr, ball_velocities):
        if(self.strength > 0):
            rand = np.random.randint(1, 4)
            # rand = 3
            if(rand % 3 == 0):
                rand2 = np.random.randint(1, 7)
                if(rand2 == 1):
                    config.falling_powerups.append(
                        ExpandPaddle(self.x, self.y, ball_velocities))
                if(rand2 == 2):
                    config.falling_powerups.append(
                        ShrinkPaddle(self.x, self.y, ball_velocities))
                if(rand2 == 3):
                    config.falling_powerups.append(FireBall(self.x, self.y, ball_velocities))
                if(rand2 == 4):
                    config.falling_powerups.append(FastBall(self.x, self.y, ball_velocities))
                if(rand2 == 5):
                    config.falling_powerups.append(ThroughBall(self.x, self.y, ball_velocities))
                if(rand2 == 6):
                    config.falling_powerups.append(ShootingPaddle(self.x, self.y, ball_velocities))
        self.strength = 0
        config.score += 10
        for i in range(brick_length):
            for j in range(brick_length):
                arr[self.y + j][self.x + i] = ' '

        if((arr[self.y-1][self.x] != ' ') and (arr[self.y-1][self.x] != ball_char) and (arr[self.y-1][self.x] != bullet_char)):
            curr = int(arr[self.y-1][self.x])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y][self.x-1] != ' ') and (arr[self.y][self.x-1] != ball_char) and (arr[self.y][self.x-1] != bullet_char)):
            curr = int(arr[self.y][self.x-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y+brick_length][self.x] != ' ') and (arr[self.y+brick_length][self.x] != ball_char) and (arr[self.y+brick_length][self.x] != bullet_char)):
            curr = int(arr[self.y+brick_length][self.x])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y+brick_length-1][self.x-1] != ' ') and (arr[self.y+brick_length-1][self.x-1] != ball_char) and (arr[self.y+brick_length-1][self.x-1] != bullet_char)):
            curr = int(arr[self.y+brick_length-1][self.x-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y][self.x+brick_length] != ' ') and (arr[self.y][self.x+brick_length] != ball_char) and (arr[self.y][self.x+brick_length] != bullet_char)):
            curr = int(arr[self.y][self.x+brick_length])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y-1][self.x+brick_length-1] != ' ') and (arr[self.y-1][self.x+brick_length-1] != ball_char) and (arr[self.y-1][self.x+brick_length-1] != bullet_char)):
            curr = int(arr[self.y-1][self.x+brick_length-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y+brick_length][self.x+brick_length-1] != ' ') and (arr[self.y+brick_length][self.x+brick_length-1] != ball_char) and (arr[self.y+brick_length][self.x+brick_length-1] != bullet_char)):
            curr = int(arr[self.y+brick_length][self.x+brick_length-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y+brick_length-1][self.x+brick_length] != ' ') and (arr[self.y+brick_length-1][self.x+brick_length] != ball_char) and (arr[self.y+brick_length-1][self.x+brick_length] != bullet_char)):
            curr = int(arr[self.y+brick_length-1][self.x+brick_length])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y-1][self.x-1] != ' ') and (arr[self.y-1][self.x-1] != ball_char) and (arr[self.y-1][self.x-1] != bullet_char)):
            curr = int(arr[self.y-1][self.x-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y-1][self.x+brick_length] != ' ') and (arr[self.y-1][self.x+brick_length] != ball_char) and (arr[self.y-1][self.x+brick_length] != bullet_char)):
            curr = int(arr[self.y-1][self.x+brick_length])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y+brick_length][self.x-1] != ' ') and (arr[self.y+brick_length][self.x-1] != ball_char) and (arr[self.y+brick_length][self.x-1] != bullet_char)):
            curr = int(arr[self.y+brick_length][self.x-1])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

        if((arr[self.y+brick_length][self.x+brick_length] != ' ') and (arr[self.y+brick_length][self.x+brick_length] != ball_char) and (arr[self.y+brick_length][self.x+brick_length] != bullet_char)):
            curr = int(arr[self.y+brick_length][self.x+brick_length])
            Brick_arr[curr].destroy(arr, Brick_arr, ball_velocities)

class BossBrick(Brick):
    pass

    def __init__(self, index):
        self.strength = np.random.randint(1, 4)
        super().__init__(index)
    
    def collision(self, arr, Brick_arr, ball_velocities):
        if (self.strength > 0):
            if(self.strength == 1):
                config.score += 10
            self.strength -= 1