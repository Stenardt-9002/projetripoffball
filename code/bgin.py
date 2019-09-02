import turtle
import random
wn = turtle.Screen()
wn.bgcolor("BLack")
wn.title("BOUNCING BALL")
wn.tracer(0) #everything on screen dissapears

colrs = ["white","red","blue","green"]

mul_bals = []
for _ in range(10):
    mul_bals.append(turtle.Turtle())

for ball in mul_bals:
    # ball = turtle.Turtle()
    ball.shape("circle")
    co_no = random.randint(0,3)
    ball.color(colrs[co_no])
    ball.penup() #doesn draw
    ball.speed(0)#animation spped
    x = random.randint(-290,290)
    y = random.randint(-290,290)
    ball.goto(x,y)
# ball.goto(0,200)
    ball.dy = 0
    ball.dx = 2 # setting x direction velocity

gravity = 0.1
while True:

    for ball in mul_bals:
        wn.update()
        ball.dy -= gravity
        ball.sety(ball.ycor()+ball.dy)

        #check for wall collision
        ball.setx(ball.xcor()+ball.dx)
        # x direction movement
        if ball.xcor()>300 or ball.xcor()<-300:
            ball.dx*=-1

        #chck bounce



        if ball.ycor()<-300:
            ball.dy*=-1



wn.mainloop() #kkeps window up
