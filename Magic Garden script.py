import pyautogui
import keyboard
import time
import threading
import sys

#define running so we can determine running state of macro
running = False

while running is None:
    time.sleep(.01)

def run_macro():
    global running
    
    if running:
        return
    
    running = True
    print('Macro started')

    while running:
        r, g, b = pyautogui.pixel(1490, 1119)
        if 110 < r < 150 and 0 <= g < 30 and 150 < b < 200:
            pyautogui.click(1490, 1119)
            time.sleep(.01)
        elif 230 < r < 256 and 195 < g < 235 and 0 <= b < 30:
            pyautogui.moveTo(1490, 1119)
            pyautogui.mouseDown(button='left')
            time.sleep(.75)
            pyautogui.mouseUp(button='left')

        # call move logic
        move_logic()
    
        time.sleep(0.1)

def move_logic():
    
    size = 10

    for row in range(size):

        if row % 2 == 0:
            key = 'd'
        else:
            key = 'a'

    for step in range(size - 1):
        keyboard.press_and_release(key)
        time.sleep(0.05)

    keyboard.press_and_release('w')
    time.sleep(0.05)

def stop():
    global running
    running = False
    print('Macro stopped')

def thread_start():
    t = threading.Thread(target=run_macro, daemon=True)
    t.start()

def hard_quit():
    print('Exiting macro')
    sys.exit()

#define hotkey so user can start and stop program
keyboard.add_hotkey('q', stop)
keyboard.add_hotkey('m', hard_quit)
keyboard.add_hotkey('p', thread_start)

print('Press p to start, q to stop, m to hard quit')

#keep the program alive w/o async
keyboard.wait()



