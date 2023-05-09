import time

import pyautogui
import keyboard

duration = 10
interval = 1

while True:
    if keyboard.is_pressed('q'):
        break
    pyautogui.moveRel(10, 0)
    pyautogui.moveRel(0, 10)
    pyautogui.moveRel(-10, 0)
    pyautogui.moveRel(0, -10)
    pyautogui.press('1')
    pyautogui.click()
    pyautogui.click()
    # pyautogui.press('Delete')
    time.sleep(5)
1