import turtle
from tkinter import messagebox
wn = turtle.Screen()
wn.title("Pong By Toby Marchant")
wn.bgcolor("black") #Makes the background color of the window black
wn.setup(width=800, height=600) #This sets the size of the window
wn.tracer(0) #This stops the window from updating, which speeds up the game because i have to manually update it

#Score
score_a = 0
score_b = 0


#Paddle A:
paddle_a = turtle.Turtle()
paddle_a.speed(0) #This is the speed of animation
paddle_a.shape("square") #This makes the shape of the paddle a square
paddle_a.color("white") #This makes the color of the paddle white
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # This stretches the width of the square, turning it into a rectangle
paddle_a.penup() #This makes the turtle not draw a line whilst moving
paddle_a.goto(-350,0) #This makes the paddle start at the left side, at -350 (The coordinates)

#Paddle B:

paddle_b = turtle.Turtle()
paddle_b.speed(0) #This is the speed of animation
paddle_b.shape("square") #This makes the shape of the paddle a square
paddle_b.color("white") #This makes the color of the paddle white
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # This stretches the width of the square, turning it into a rectangle
paddle_b.penup() #This makes the turtle not draw a line whilst moving
paddle_b.goto(350,0) ##This makes the paddle start at the right side, at +350 (The coordinates)

#The paddles are 100 pixles tall by 20 pixels wide

#Ball:

ball = turtle.Turtle()
ball.speed(0) #This is the speed of animation
ball.shape("square") #This makes the shape of the paddle a square
ball.color("white") #This makes the color of the paddle white
ball.penup() #This makes the turtle not draw a line whilst moving
ball.goto(0,0) #This makes the ball start at the middle point, which is 0,0
ball.dx = 0.15 #This means every time the ball moves it moves two pixels too the right, as it is negative 
ball.dy = -0.15 #This means every time the ball moves it moves two pixels up 
#Dx means change

#Pen
pen = turtle.Turtle() #This
pen.speed(0) #This is the animation speed
pen.color("white") #This is the colour of the Score
pen.penup() #This hides the line being drawn
pen.hideturtle() #This hides the turtle drawing
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))




#Function:

def paddle_a_up():
    y = paddle_a.ycor() #The y cor method is from the turtle module, and what it does is return the y coordinate, so i have assigned it to this variable called y.
    y += 20 #This adds 20 pixels to the y coordinate
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor() #The y cor method is from the turtle module, and what it does is return the y coordinate, so i have assigned it to this variable called y.
    y -= 20 #This  20 pixels to the y coordinate
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor() #The y cor method is from the turtle module, and what it does is return the y coordinate, so i have assigned it to this variable called y.
    y += 20 #This adds 20 pixels to the y coordinate
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor() #The y cor method is from the turtle module, and what it does is return the y coordinate, so i have assigned it to this variable called y.
    y -= 20 #This  20 pixels to the y coordinate
    paddle_b.sety(y)



#Keyboard binding:

wn.listen() #This tells the turtle module to listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w") #This lines means that when the users enters "w" call the function "paddle_a_up" which then runs all the code in the function, which allows the user to move the paddle up.
wn.onkeypress(paddle_a_down, "s") #This lines means that when the users enters "s" call the function "paddle_a_down" which then runs all the code in the function, which allows the user to move the paddle down.
wn.onkeypress(paddle_b_up, "Up") #This lines means that when the users enters the up arrow key, call the function "paddle_b_up" which then runs all the code in the function, which allows the user to move the paddle up.
wn.onkeypress(paddle_b_down, "Down") #This lines means that when the users enters the bottom arrow key, call the function "paddle_b_down" which then runs all the code in the function, which allows the user to move the paddle down.

#Main Game Loop:

while True:
    wn.update() #What this does, is it updates the screen every time the program is run.

    #Move the ball
    ball.setx(ball.xcor() + ball.dx) # This means the ball starts at 0,0 x, and the first time it goes through this loop above, its going to 2, then 2 etc.
    ball.sety(ball.ycor() + ball.dy) # This means the ball starts at 0,0 x, and the first time it goes through this loop above, its going to 2, then 2 etc.

    #Border Checking:
    if ball.ycor() > 290:
        ball.sety(290) #This sets the ball back to 290
        ball.dy *= -1 #This reverses the direction of the ball
    if ball.ycor() < -290:
        ball.sety(-290) #This sets the ball back to 290
        ball.dy *= -1 #This reverses the direction of the ball
    if ball.xcor() > 390: #This tells us it has gone past the paddle and is off the screen
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1 #This means that if the ball goes off to the right side then player a will get 1 point added to there score
        pen.clear() #This clears the score on the screen before the game has started, otherwise a 0 would be printed and every time someone would score a point it would go over that number 0
        pen.write("Player A: {} Player B: {}". format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #By formating this. it means that teh score from a and b will be put into the {} for either player a or b, depending on who wins the point
    if ball.xcor() < -390: #This tells us it has gone past the paddle and is off the screen
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 #This means that if the ball goes off to the left side then player b will get 1 point added to there score
        pen.clear() #This clears the score on the screen before the game has started, otherwise a 0 would be printed and every time someone would score a point it would go over that number 0
        pen.write("Player A: {} Player B: {}". format(score_a, score_b), align="center", font=("Courier", 24, "normal")) #By formating this. it means that teh score from a and b will be put into the {} for either player a or b, depending on who wins the point

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40): #This means the edges are basically touching, and is the ball between the top of the paddle and the bottom of the paddle
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40): #This means the edges are basically touching, and is the ball between the top of the paddle and the bottom of the paddle
        ball.setx(-340)
        ball.dx *= -1


