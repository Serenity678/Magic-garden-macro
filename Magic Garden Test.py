import pyautogui
import time

print(pyautogui.size())
time.sleep(3)
print(pyautogui.position())
print(pyautogui.pixel(*pyautogui.position()))

