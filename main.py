import utility_aew_caw as util
import turtle
import random
import time
import sys
sys.path.append('./modules')
from pynput.keyboard import Key, Listener

screen = turtle.Screen()
util.setup_screen(screen)
ori = turtle.Turtle()
util.setup_turtle(ori)

player1_fired = False
player2_fired = False
round_started = False

def on_press(key):
    if key == Key.space and util.has_focus(screen):
        if not round_started:
            #round_started = True
            start_round()
    try:
        if key.char == 'z' and util.has_focus(screen):
            player1_fired = True
        elif key.char == 'm' and util.has_focus(screen):
            player2_fired = True
        # detect space key to start a new round
    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char == 'z' and util.has_focus(screen):
            player1_fired = False
        elif key.char == 'm' and util.has_focus(screen):
            player2_fired = False
    except AttributeError:
        pass

listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

player1_score = 0
player2_score = 0

def point(player):
    if player == 1:
        player1_score += 1
    else:
        player2_score += 1
    util.draw_scores(ori, player1_score, player2_score)

def start_round():
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
        print(time.time() - start_time)
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



def __main__():
    util.draw_text(ori, "Press space to start a new round")

__main__()

turtle.done()