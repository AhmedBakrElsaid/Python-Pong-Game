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

#functions
def madrab01_up():
    y = madrab01.ycor()
    y += 20
    madrab01.sety(y)

#keyboard bindings

window.listen()
window.onkeypress(madrab01_up,'w')


while True:
    window.update()