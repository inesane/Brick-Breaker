# Brick-Breaker

## Terminal Based Brick Breaker Game

## To Run:

Make sure that numpy and colorama are installed

```
python3 main.py
```
## How To Play:

1. Game Starts. There are 3 levels. Move Paddle with 'a' to go left and 'd' to go right. Release ball with 'w'. Go to next level with 'c'.

2. Red Bricks have strength 3, yellow have strength 2, green have strength 1, grey are unbreakable and purple are explosive (destroy adjacent/diagonal bricks). Rainbow bricks constantly change strength until hit. After a certain period of time, bricks start dropping by one place each time the ball comes in contact with the paddle and if the bricks reach the paddle, the game is over.

3. 10 points added per brick broken.

4. Each round has 3 lives. Lives get lost when the ball is missed by the paddle or paddle is hit by a bomb by the boss in the 3rd level.

5. Upon destroying a block, there is a chance of a powerup spawning with a gravity effect so that they fall towards the bottom of the screen. Catch the powerups with your paddle to activate them. There are 6 powerups. Expand Paddle (increases paddle length), Shrink Paddle (decreases paddle length), Fast Ball (increases ball velocity), Through Ball (passes through and destroys all bricks that come in the way), Shooting Paddle (changes color of paddle and shoots bullets from the ends of the paddle which damage the bricks similar to the ball) and Fireball (makes brick that is in contact with ball explosive).

6. Levels 1 and 2 end when all bricks except for unreakable bricks are destroyed.

7. Level 3 has a boss who regularly drops bombs. Bombs upon hitting your paddle makes you lose a life. The Boss has a certain health and hitting the boss with your ball decreases its health. Upon reaching 2/3rd and 1/3rd of total health, the boss spawns a protective layer of bricks. Level 3 ends when the boss looses all his health.

8. Game ends when all lives are lost or all levels are passed. You can also press 'x' to end game

## OOPS Concepts:

1. Inheritance - Breakable, Unbreakable and Exploding Bricks all inherit from parent class Brick. ExpandPaddle, ShrinkPaddle, FastBall and ThroughBall powerups all inherit from parent class PowerUp

2. Polymorphism - Collision function of Exploding Bricks overrides the initial collision function from parent class Brick

3. Encapsulation - Classes for Ball, Paddle, Brick, Powerup

4. Abstraction - Each class has functions, such as destroy() and collide() for Brick and move() for Paddle and Ball