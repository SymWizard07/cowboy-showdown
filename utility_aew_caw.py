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

def done():
    turtle.done()

#cowboy function
def cowboy():
    pass