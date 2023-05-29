import turtle
import winsound

window = turtle.Screen() #create window
window.title("Ping-Pong") #title for window
window.bgcolor("black") #background color for window
window.setup(width=800, height=600) #window stats
window.tracer(0) #stop window updates; update manually speeds up game




#Movement
def paddle_left_up():
    y = paddle_left.ycor() #current y coordinate of paddle_left
    y += 20 #add 20px
    paddle_left.sety(y) #set new position y of paddle_left

def paddle_left_down():
    y = paddle_left.ycor() #current y coordinate of paddle_left
    y -= 20 #sub 20px
    paddle_left.sety(y) #set new position y of paddle_left

def paddle_right_up():
    y = paddle_right.ycor() #current y coordinate of paddle_right
    y += 20 #add 20px
    paddle_right.sety(y) #set new position y of paddle_right

def paddle_right_down():
    y = paddle_right.ycor() #current y coordinate of paddle_right
    y -= 20 #sub 20px
    paddle_right.sety(y) #set new position y of paddle_right

#Game Control
game_status = "splash"

def startGame():
    global game_status
    game_status = "game"

    #Paddle Left
    global paddle_left
    paddle_left = turtle.Turtle() #Turtle object
    paddle_left.speed(0) #speed of animation; set to maximum
    paddle_left.shape("square") #giving paddle a shape
    paddle_left.color("white") #giving paddle a color
    paddle_left.shapesize(stretch_wid=5, stretch_len=1) #stretching/giving right size to paddle
    paddle_left.penup() #lifting a 'pen' up to stop drawing and be able to move paddle without drawing
    paddle_left.goto(-350, 0) #alocating paddle on screen


    #Paddle Right
    global paddle_right
    paddle_right = turtle.Turtle() #Turtle object
    paddle_right.speed(0) #speed of animation; set to maximum
    paddle_right.shape("square") #giving paddle a shape
    paddle_right.color("white") #giving paddle a color
    paddle_right.shapesize(stretch_wid=5, stretch_len=1) #stretching/giving right size to paddle
    paddle_right.penup() #lifting a 'pen' up to stop drawing and be able to move paddle without drawing
    paddle_right.goto(350, 0) #alocating paddle on screen

    #Ball
    global ball
    ball = turtle.Turtle() #Turtle object
    ball.speed(0) #speed of animation; set to maximum
    ball.shape("turtle") #giving ball a shape
    ball.color("white") #giving ball a color
    ball.penup() #lifting a 'pen' up to stop drawing and be able to move ball without drawing
    ball.goto(0, 0) #alocating ball starting position on screen
    ball.dx = 0.2 #change of ball speed in x axis; moves by 2px
    ball.dy = 0.2 #change of ball speed in y axis; moves by 2px

    #Scoring
    global score1
    global score2
    score1 = 0
    score2 = 0
    global pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player 1: 0                                   Player 2: 0", align="center", font=("Cpurier", 24, "normal"))

#Keybinding
window.listen() #listen for keyboard input
window.onkeypress(paddle_left_up, "w") #when 'w' is pressed call the function
window.onkeypress(paddle_left_down, "s") #when 's' is pressed call the function
window.onkeypress(paddle_right_up, "Up") #when 'Up' is pressed call the function
window.onkeypress(paddle_right_down, "Down") #when 'Down' is pressed call the function

window.onkeypress(startGame, "space")

#Main game loop
while True:
    if game_status == "splash":
        window.bgpic("menu.gif")
    elif game_status == "game":
        window.bgpic("game.gif")
        #Ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #Screen collision
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.dy *= -1
            winsound.PlaySound("E:\PythonZadania\Projekt3\\bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score1 += 1
            pen.clear()
            pen.write("Player 1: {}                                   Player 2: {}".format(score1, score2), align="center", font=("Cpurier", 24, "normal"))


        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score2 += 1
            pen.clear()
            pen.write("Player 1: {}                                   Player 2: {}".format(score1, score2), align="center", font=("Cpurier", 24, "normal"))

        #Paddle collision
        if ball.xcor() > 340 and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
            ball.dx *= -1
            ball.dy *= -1
            winsound.PlaySound("E:\PythonZadania\Projekt3\\bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() < -340 and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
            ball.dx *= -1
            ball.dy *= -1
            winsound.PlaySound("E:\PythonZadania\Projekt3\\bounce.wav", winsound.SND_ASYNC)

        if score1 == 3:
            game_status = "gameover"
            print(game_status)
        elif score2 == 3:
            game_status = "gameover"
            print(game_status)

    elif game_status == "gameover":
        #turtle.reset()
        ball.reset()
        paddle_left.reset()
        paddle_right.reset()
        pen.reset()
        if score1 == 3:
            window.bgpic("player1.gif")       
        elif score2 == 3:
            window.bgpic("player2.gif")

    window.update() #update screen

    