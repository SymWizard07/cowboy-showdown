import utility_aew_caw as util
import cowboy_utility_aew_caw as cowboy_util
import turtle
import random
import time
import sys
sys.path.append('./modules')
from pynput.keyboard import Key, Listener


print("Would you like to play against a friend or the computer?")
print("1. Friend")
print("2. Computer")
is_computer = False

while True:
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("You have chosen to play against a friend.")
        print("Player 1: Press 'z' to fire")
        print("Player 2: Press 'm' to fire")
        break
    elif choice == "2":
        print("You have chosen to play against the computer.")
        print("Player 1: Press 'z' to fire")
        is_computer = True
        break
    print("Only enter a 1 or 2.")
    

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
        elif player2_fired and not is_computer:
            point(1)
            util.draw_text(ori, "Player 2 shot too early!")
            return
        turtle.update()
        time.sleep(0.01)
    # display draw text. A user who fires in this period will win a point.
    computer_reaction_time = random.randint(450, 800) / 1000
    draw_time = time.time()
    util.draw_text(ori, "Draw!")
    while True:
        if player1_fired:
            cowboy_util.explosion(ori, True)
            point(1)
            util.draw_text(ori, "Player 1 wins!")
            return
        elif player2_fired and not is_computer:
            cowboy_util.explosion(ori, False)
            point(2)
            util.draw_text(ori, "Player 2 wins!")
            return
        elif time.time() - draw_time > computer_reaction_time and is_computer:
            cowboy_util.explosion(ori, False)
            point(2)
            util.draw_text(ori, "Computer wins!")
            return
        turtle.update()
        time.sleep(0.01)

def on_press(key):
    global player1_fired, player2_fired, space_pressed
    if key == Key.space:
        space_pressed = True
    try:
        if key.char == 'z':
            player1_fired = True
        elif key.char == 'm':
            player2_fired = True
    except AttributeError:
        pass

def on_release(key):
    global player1_fired, player2_fired, space_pressed
    if key == Key.space:
        space_pressed = False
    try:
        if key.char == 'z':
            player1_fired = False
        elif key.char == 'm':
            player2_fired = False
    except AttributeError:
        pass

listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

def main():
    cowboy_util.player1(ori)
    cowboy_util.player2(ori)
    util.draw_scores(ori, player1_score, player2_score)
    util.draw_text(ori, "Press space to start a new round")
    while True:
        if space_pressed:
            start_round()
            time.sleep(2)
            util.draw_text(ori, "Press space to start a new round")
        turtle.update()
        time.sleep(0.1)

if __name__ == "__main__":
    main()
    turtle.done()