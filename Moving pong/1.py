import turtle

window1 = turtle.Screen() #singleton class
window1.title("Ball game")
window1.bgcolor("black")
window1.setup(width = 800,height = 600)
window1.tracer(0) #If n is given, only each n-th regular screen update is really performed.


ball_1 = turtle.Turtle()
ball_1.speed(0)
ball_1.shape("circle") # 20 pixels length
ball_1.color("white")
ball_1.penup()#draw movement wont be shown
# ball_1.goto(-350,0)
# ball_1.shapesize(stretch_wid=6 ,stretch_len=1)
ball_1 .dx = .1
ball_1 .dy = .1 #//velocity




# //stick a ,b ball
stick_1 = turtle.Turtle()
stick_1.speed(0)
stick_1.shape("square") # 20 pixels length
stick_1.color("green")
stick_1.penup()#draw movement wont be shown
stick_1.goto(-350,0)
stick_1.shapesize(stretch_wid=6 ,stretch_len=1)
 #right has positice x
stick_2 = turtle.Turtle()
stick_2.speed(0)
stick_2.shape("square") # 20 pixels length
stick_2.color("red")
stick_2.penup()#draw movement wont be shown
stick_2.goto(350,0)
stick_2.shapesize(stretch_wid=6 ,stretch_len=1)


# def mooveobject_1():
#     y = stick_1.ycor()
#     y+=20
#     stick_1.sety(y)
# def mooveobjectdown_1():
#     y = stick_1.ycor()
#     y-=20
#     stick_1.sety(y)
window1.listen()
# window1.onkeypress(mooveobject_1,"w")
# window1.onkeypress(mooveobjectdown_1,"s")
window1.onkeypress(lambda:stick_1.sety(stick_1.ycor()+20 if stick_1.ycor()<240 else stick_1.ycor()),"w")
# window1.onkeypress(lambda:stick_1.sety(stick_1.ycor()-20),"s")
window1.onkeypress(lambda:stick_1.sety(stick_1.ycor()-20 if stick_1.ycor()>-240 else stick_1.ycor()),"s")

# window1.onkeypress(lambda:stick_2.sety(stick_2.ycor()+20) if(stick_2.ycor()<600),"Up")
window1.onkeypress(lambda:stick_2.sety(stick_2.ycor()+20 if stick_2.ycor()<240 else stick_2.ycor()) ,"Up")

window1.onkeypress(lambda:stick_2.sety(stick_2.ycor()-20 if stick_2.ycor()>-240 else stick_2.ycor()),"Down")



while True:
    window1.update()
    # ball_1.setx(lambda :ball_1.xcor()+ball_1.dx if (ball_1.xcor()>260 or ball_1.xcor()<-260) else ball_1.dx=-ball_1.dx )
    # ball_1.sety(ball_1.ycor()+ball_1.dy if (ball_1.ycor()>240 or ball_1.ycor()<-240) else ball_1.dy=-ball_1.dy )
    # ball_1.setx(ball_1.xcor()+ball_1.dx if (ball_1.xcor()>260 or ball_1.xcor()<-260) else ball_1.dx=-ball_1.dx )

    ball_1.setx(ball_1.xcor()+ball_1.dx)

    ball_1.sety(ball_1.ycor()+ball_1.dy)

    # border
    if ball_1.ycor()>240 or ball_1.ycor()<-240:
        # ball_1.sety(40)
        ball_1.dy*=-1

    if ball_1.xcor()>310 or ball_1.xcor()<-310:
        # ball_1.setx(290)
        ball_1.dx*=-1
#22:34
