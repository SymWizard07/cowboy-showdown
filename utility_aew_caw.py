import turtle

#setup_window() function
def setup_window():
    window = turtle.Screen()
    window.setup(1000,600)
    window.bgcolor("orange")
    window.title("Cowboy Showdown")
    return window

#setup_turtle() function
def setup_turtle():
    ori = turtle.Turtle()
    ori.shape("turtle")
    ori.pencolor("black")
    ori.pensize(5)
    ori.speed(0)
    return ori

#cowboy function
def cowboy():
    