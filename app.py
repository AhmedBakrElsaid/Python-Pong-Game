# import Turtule Module
import turtle

window = turtle.Screen()
window.title("Ping Pong BY Python")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


madrab01 = turtle.Turtle()
madrab01.speed(0)
madrab01.shape("square")
madrab01.color("blue")
madrab01.shapesize(stretch_wid=5,stretch_len=1)
madrab01.penup()
madrab01.goto(-350,0)


madrab02 = turtle.Turtle()
madrab02.speed(0)
madrab02.shape("square")
madrab02.color("red")
madrab02.shapesize(stretch_wid=5,stretch_len=1)
madrab02.penup()
madrab02.goto(350,0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1


# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player1 : 0 player2 : 0",align='center',font=('courier',24,'normal'))

#functions
def madrab01_up():
    y = madrab01.ycor()
    y += 20
    madrab01.sety(y)

def madrab01_down():
    y = madrab01.ycor()
    y -= 20
    madrab01.sety(y)

def madrab02_up():
    y = madrab02.ycor()
    y += 20
    madrab02.sety(y)

def madrab02_down():
    y = madrab02.ycor()
    y -= 20
    madrab02.sety(y)


#keyboard bindings

window.listen()
window.onkeypress(madrab01_up,'w')
window.onkeypress(madrab01_down,'s')
window.onkeypress(madrab02_up,'Up')
window.onkeypress(madrab02_down,'Down')


while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player1 : {} player2 : {}".format(score1,score2),align='center',font=('courier',24,'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player1 : {} player2 : {}".format(score1,score2),align='center',font=('courier',24,'normal'))

    # ball touches madrabs
    if (ball.xcor()> 340 and ball.xcor() < 350) and (ball.ycor() < madrab02.ycor() +40 and ball.ycor() > madrab02.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrab01.ycor() +40 and ball.ycor() > madrab01.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    