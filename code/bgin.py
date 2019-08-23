import turtle

wn = turtle.Screen()
wn.bgcolor("BLack")
wn.title("BOUNCING BALL")
wn.tracer(0) #everything on screen dissapears



ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.speed(0)#animation spped
ball.goto(0,200)
# ball.goto(0,200)
ball.dy = 0
ball.dx = 2 # setting x direction velocity

gravity = 0.1
while True:
    wn.update()
    ball.dy -= gravity 
    ball.sety(ball.ycor()+ball.dy)

    #check for wall collision
    ball.setx(ball.xcor()+ball.dx)
    if ball.xcor()>300 or ball.xcor()<-300:
        ball.dx*=-1

    #chck bounce



    if ball.ycor()<-300:
        ball.dy*=-1



wn.mainloop()
