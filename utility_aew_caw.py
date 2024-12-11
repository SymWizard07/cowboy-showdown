import turtle

#setup_window() function
def setup_screen(screen):
    screen.setup(1000,600)
    screen.bgcolor("orange")
    screen.title("Cowboy Showdown")
    return screen

#check for window focus
def has_focus(screen):
    root = screen.getcanvas().winfo_toplevel()
    return screen._root.focus_get() == screen._root

#setup_turtle() function
def setup_turtle(ori):
    ori.shape("turtle")
    ori.pencolor("black")
    ori.pensize(5)
    ori.speed(0)
    return ori

def draw_text(ori, text):
    clear_text(ori)
    ori.penup()
    ori.goto(0, 150)
    ori.pendown()
    ori.fillcolor("black")
    ori.color("black")
    ori.write(text, font=("Courier", 32, "bold"), align="center")

def clear_text(ori):
    # draw rectangle over previous text
    rect_size = 1000
    ori.penup()
    ori.goto(-1 * (rect_size / 2), 200)
    ori.pendown()
    ori.fillcolor("orange")
    ori.color("orange")
    ori.begin_fill()
    for i in range(2):
        ori.forward(rect_size)
        ori.right(90)
        ori.forward(50)
        ori.right(90)
    ori.end_fill()

# draw scores for each player on the left and right side of the top of the screen.
def draw_scores(ori, player1_score, player2_score):
    # draw rectangle over previous text
    rect_size = 150
    ori.penup()
    ori.goto(-1 * (rect_size / 2), 300)
    ori.pendown()
    ori.fillcolor("orange")
    ori.color("orange")
    ori.begin_fill()
    for i in range(2):
        ori.forward(rect_size)
        ori.right(90)
        ori.forward(50)
        ori.right(90)
    ori.end_fill()
    ori.penup()
    ori.goto(-1 * (rect_size / 2), 300)
    ori.pendown()
    ori.fillcolor("black")
    ori.color("black")
    ori.write("Player 1: " + str(player1_score), font=("Courier", 24, "bold"), align="center")
    ori.penup()
    ori.goto(0, 300)
    ori.pendown()
    ori.fillcolor("orange")
    ori.color("orange")
    ori.begin_fill()
    for i in range(2):
        ori.forward(rect_size)
        ori.right(90)
        ori.forward(50)
        ori.right(90)
    ori.end_fill()
    ori.penup()
    ori.goto(0, 300)
    ori.pendown()
    ori.fillcolor("black")
    ori.color("black")
    ori.write("Player 2: " + str(player2_score), font=("Courier", 24, "bold"), align="center")

def done():
    turtle.done()

#cowboy function
def cowboy():
    pass