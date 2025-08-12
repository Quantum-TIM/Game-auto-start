import pyautogui
import time
from datetime import datetime
import keyboard

pyautogui.useImageNotFoundException()

while True:
    try:
        # locate the auto start condition image
        start = pyautogui.locateOnScreen("D:\Workspace\python\Projects\RDR2_starter\story.png", confidence=0.7)
        if start:
            time.sleep(4)
            keyboard.press_and_release('enter') # trigger key to start the game
            with open('game_start.txt', 'a+') as file:
                cont = f"Game started at: {datetime.now()}\n"
                file.write(cont)
            break
        else:
            time.sleep(3)
            with open('game_start.png', 'a+') as file:
                file.write(f"Game couldn't {datetime.now()}")
    # sadly you will face this error often
    except pyautogui.ImageNotFoundException:
        pass
