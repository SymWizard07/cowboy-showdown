import utility_aew_caw as util
import turtle
import sys
sys.path.append('./modules')
from pynput.keyboard import Key, Listener

screen = turtle.Screen()
util.setup_screen(screen)
ori = turtle.Turtle()
util.setup_turtle(ori)

def on_press(key):
    try:
        if key.char == 'z' and util.has_focus(screen):
            print("Pow!")
    except AttributeError:
        pass

def on_release(key):
    pass

listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

def __main__():
    pass

__main__()

turtle.done()