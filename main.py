import utility_aew_caw as util
import turtle
import random
import time
import threading
import sys
sys.path.append('./modules')
from pynput.keyboard import Key, Listener

screen = turtle.Screen()
util.setup_screen(screen)
ori = turtle.Turtle()
util.setup_turtle(ori)

player1_fired = False
player2_fired = False
player1_score = 0
player2_score = 0
space_pressed = False
round_started = False

def point(player):
    global player1_score, player2_score
    if player == 1:
        player1_score += 1
    else:
        player2_score += 1
    util.draw_scores(ori, player1_score, player2_score)

def start_round():
    global player1_fired, player2_fired
    # display prepare text. A user who fires in this period will lose.
    util.draw_text(ori, "Ready...")
    start_time = time.time()
    # randomize time until draw
    duration = random.randint(3, 5)
    while time.time() - start_time < duration:
        # clear ready text after 2 seconds
        if time.time() - start_time > 2:
            util.clear_text(ori)
        if player1_fired:
            point(2)
            util.draw_text(ori, "Player 1 shot too early!")
            return
        elif player2_fired:
            point(1)
            util.draw_text(ori, "Player 2 shot too early!")
            return
        #print(player1_fired)
        time.sleep(0.1)
    # display draw text. A user who fires in this period will win a point.
    util.draw_text(ori, "Draw!")
    while not player1_fired and not player2_fired:
        if player1_fired:
            point(1)
            util.draw_text(ori, "Player 1 wins!")
            return
        elif player2_fired:
            point(2)
            util.draw_text(ori, "Player 2 wins!")
            return
        time.sleep(0.1)

def on_press(key):
    global player1_fired, player2_fired, space_pressed
    if key == Key.space and util.has_focus(screen):
        space_pressed = True
    try:
        if key.char == 'z' and util.has_focus(screen):
            player1_fired = True
        elif key.char == 'm' and util.has_focus(screen):
            player2_fired = True
        # detect space key to start a new round
    except AttributeError:
        pass

def on_release(key):
    global space_pressed
    if key == Key.space:
        space_pressed = False
    try:
        if key.char == 'z':
            pass
            #player1_fired = False
        elif key.char == 'm':
            pass
            #player2_fired = False
    except AttributeError:
        pass

listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

def __main__():
    util.draw_text(ori, "Press space to start a new round")
    while True:
        if space_pressed:
            round_started = True
            start_round()
        time.sleep(1)

__main__()
turtle.done()