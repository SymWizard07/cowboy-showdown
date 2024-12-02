import utility_aew_caw as util
from modules import keyboard # type: ignore
print(keyboard.__file__)

def __main__():
    while True:
        if keyboard.is_pressed('q'):
            print("you pressed q")

__main__()