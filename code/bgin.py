import turtle

wn = turtle.Screen()
wn.bgcolor("BLack")
wn.title("BOUNCING BALL")

ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.speed(0)#animation spped
ball.goto(0,200)
# ball.goto(0,200)
ball.dy = 0

gravity = 0.1
while True:
    ball.dy -= gravity 
    ball.sety(ball.ycor()+ball.dy)
    #chck bounce
    if ball.ycor()<-300:
        ball.dy*=-1



wn.mainloop()
