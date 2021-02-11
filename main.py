import colorama, copy

from input import input_to, Get

import numpy as np

rows = 30
columns = 30
fps = 30
t = 1/fps

class Paddle:
    def __init__(self, length, height):
        super().__init__()
        self.length = length
        self.height = height
        self.x = 10
        self.y = 20
        self.vel = 1

    def disp(self, arr):
        length = self.length
        height = self.height
        x = self.x
        y = self.y
        for i in range(x, x+length):
            arr[rows-1][i] = '='

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

newPaddle = Paddle (6,1)

while True:
    key = input_to(Get())

    board = np.full((rows, columns+1), " ")

    for i in range (rows):
        board[i][columns]='\n'
    print("\033[H\033[J", end="")

    newPaddle.disp(board)

    for i in board:
        for j in i:
            print(j, end="")

    if(key == "d" or key == "a"):
        newPaddle.move(key)
        # print(newPaddle.x)
        # print(newPaddle.length)
        # print(columns)
        # newPaddle.disp(board)
        # for i in board:
        #     for j in i:
        #         print(j, end="")

    if(key == "x"):
        quit()