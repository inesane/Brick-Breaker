# Brick-Breaker

## Terminal Based Brick Breaker Game

## To Run:

Make sure that numpy and colorama are installed

```
python3 main.py
```
## How To Play:

1. Game Starts. Move Paddle with 'a' to go left and 'd' to go right. Release ball with 'w'.

2. Red Bricks have strength 3, yellow have strength 2, green have strength 1, grey are unbreakable and purple are explosive (destroy adjacent/diagonal bricks)

3. 10 points added per brick broken

4. Each round has 3 lives. Lives get lost when the ball is missed by the paddle.

5. Upon destroying a block, there is a chance of a powerup spawning. Catch the powerups with your paddle to activate them. There are 4 powerups. Expand Paddle (increases paddle length), Shrink Paddle (decreases paddle length), Fast Ball (increases ball velocity) and Through Ball (passes through and destroys all bricks that come in the way).

6. Game ends when all lives are lost or all breakable and explosive bricks are destroyed. You can also press 'x' to end game

## OOPS Concepts:

1. Inheritance - Breakable, Unbreakable and Exploding Bricks all inherit from parent class Brick. ExpandPaddle, ShrinkPaddle, BallMultiplier, FastBall, ThroughBall and PaddleGrab powerups all inherit from parent class PowerUp

2. Polymorphism - Collision function of Exploding Bricks overrides the initial collision function from parent class Brick

3. Encapsulation - Classes for Ball, Paddle, Brick, Powerup

4. Abstraction - Each class has functions, such as destroy() and collide() for Brick and move() for Paddle and Ball