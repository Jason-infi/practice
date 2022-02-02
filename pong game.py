import functools
import turtle


#function to create a turtle window
def create_window(width,height,bgcolor,title):

    window = turtle.Screen()
    window.bgcolor(bgcolor)
    window.title(title)
    window.setup(width,height)
    window.tracer(0)

    return window

#creating a 1200x720 window
window = create_window(width=1200,height=720,bgcolor='black',title='pong game python')

#function to create a turtle object
def create_turtle(shape,color,x,y,str_len,str_wid):
    paddle = turtle.Turtle()
    paddle.shape(shape)
    paddle.color(color)
    paddle.penup()
    paddle.speed(0)
    paddle.goto(x,y)
    paddle.shapesize(stretch_len=str_len,stretch_wid=str_wid)

    return paddle

#creating paddles and ball objects using create_turtle function
paddle_1 = create_turtle(shape='square',color='cyan',x=-540,y=0,str_len=1,str_wid=5)
paddle_2 = create_turtle(shape='square',color='cyan',x=540,y=0,str_len=1,str_wid=5)
ball = create_turtle('circle','yellow',0,0,1,1)

#setting initial scores to 0
score_p1 = 0
score_p2 = 0

#defining delta x and y to accelerate the ball
ball.dx = 0.2
ball.dy = -0.2

#creating a object to display scoreboard on the window
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color('pink')
pen.goto(0,320)
pen.speed(0)
pen.write('Player 1 : 0 Player 2 : 0',align='center',font=('Courier',18,'normal'))

#function to move paddle's up and down
def move_turtle(my_turtle,direction):
    if direction == 'up':
        y = my_turtle.ycor()
        if y < 350 :
            y = y + 20
            my_turtle.sety(y)
    elif direction == 'down':
        y = my_turtle.ycor()
        if y > -350:
            y = y - 20
            my_turtle.sety(y)


#defining actions to control the paddles
window.listen()
window.onkeypress(functools.partial(move_turtle,paddle_1,'up'),'w')
window.onkeypress(functools.partial(move_turtle,paddle_2,'up'),'Up')
window.onkeypress(functools.partial(move_turtle,paddle_1,'down'),'s')
window.onkeypress(functools.partial(move_turtle,paddle_2,'down'),'Down')



while True:

    window.update()

    #moving the ball initially    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #bouncing ball if it touches the top of the window
    if ball.ycor() > 350:
        ball.dy *= -1
    
    #bouncing ball if it touches the bottom of the window
    if ball.ycor() < -350:
        ball.dy *= -1
    
    #crediting points to other player if player 2 doesn't catch the ball and resetting the ball position to the center
    if ball.xcor() > 590:
        score_p1 +=1
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        pen.write(f'Player 1 : {score_p1} Player 2 : {score_p2}',align='center',font=('Courier',18,'normal'))
    
    #crediting points to other player if player 1 doesn't catch the ball and resetting the ball position to the center
    if ball.xcor() < -590:
        score_p2 +=1
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        pen.write(f'Player 1 : {score_p1} Player 2 : {score_p2}',align='center',font=('Courier',18,'normal'))    
    

    #conditions to detect if the ball touches the paddle or not
    if (ball.xcor() > 530 and ball.xcor() < 540) and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor()-50):
        ball.setx(530)
        ball.dx *= -1
    
    if (ball.xcor() < -530 and ball.xcor() > -540) and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor()-50):
        ball.setx(-530)
        ball.dx *= -1