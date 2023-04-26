from random import randint

import turtle


screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("white")
screen.setup(width=1000,
             height=600)

leftPad = turtle.Turtle()
leftPad.speed(0)
leftPad.shape("square")
leftPad.color("black")
leftPad.shapesize(stretch_wid=6,
                  stretch_len=0.5)
leftPad.penup()
leftPad.goto(-400, 0)

rightPad = turtle.Turtle()
rightPad.speed(0)
rightPad.shape("square")
rightPad.color("black")
rightPad.shapesize(stretch_wid=6,
                   stretch_len=0.5)
rightPad.penup()
rightPad.goto(400, 0)

hitBall = turtle.Turtle()
hitBall.speed(40)
hitBall.shape("circle")
hitBall.color("red")
hitBall.penup()
hitBall.goto(0, 0)
hitBall.dx = 5
hitBall.dy = -5

# scores
leftPlayer = 0
rightPlayer = 0

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left : 0    Right: 0",
             align="center", font=("Courier", 24, "normal"))


def lpaddleUp():
    y = leftPad.ycor()
    y += 20
    leftPad.sety(y)
 
def lpaddleDown():
    y = leftPad.ycor()
    y -= 20
    leftPad.sety(y)
    
def rpaddleUp():
    y = rightPad.ycor()
    y += 20
    rightPad.sety(y)
 
def rpaddleDown():
    y = rightPad.ycor()
    y -= 20
    rightPad.sety(y)    

screen.listen()
screen.onkeypress(rpaddleUp, "a")
screen.onkeypress(rpaddleDown, "d")
screen.onkeypress(lpaddleUp, "Up")
screen.onkeypress(lpaddleDown, "Down")



while True:

    print(hitBall.xcor(), hitBall.ycor())

    screen.update()

    hitBall.setx(hitBall.xcor() + hitBall.dx)
    hitBall.sety(hitBall.ycor() + hitBall.dy)

    if hitBall.ycor() > 280:
        hitBall.sety(280)
        hitBall.dy *= -1

    if hitBall.ycor() < -280:
        hitBall.sety(-280)
        hitBall.dy *= -1

    if hitBall.xcor() > 500:
        hitBall.goto(0, 0)
        hitBall.dy = abs(hitBall.dy) / hitBall.dy
        hitBall.dy *= -1 * randint(0, 20)
        leftPlayer += 1
        sketch.clear()
        sketch.write("Left : {}    Right: {}".format(
            leftPlayer, rightPlayer), align="center",
            font=("Courier", 24, "normal"))

    if hitBall.xcor() < -500:
        hitBall.goto(0, 0)
        hitBall.dy = abs(hitBall.dy) / hitBall.dy
        hitBall.dy *= -1 * randint(0, 20)
        rightPlayer += 1
        sketch.clear()
        sketch.write("Left : {}    Right: {}".format(
            leftPlayer, rightPlayer), align="center",
            font=("Courier", 24, "normal"))

    if ((hitBall.xcor() > 360 and
         hitBall.xcor() < 362.5) and
            (hitBall.ycor() < rightPad.ycor() + 40 and
             hitBall.ycor() > rightPad.ycor() - 40)):
        hitBall.setx(360)
        hitBall.dx *= -1

    if ((hitBall.xcor() < -360 and
         hitBall.xcor() > -362.5) and
            (hitBall.ycor() < leftPad.ycor() + 40 and
             hitBall.ycor() > leftPad.ycor() - 40)):
        hitBall.setx(-360)
        hitBall.dx*= -1
        

