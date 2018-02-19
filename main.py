import pyautogui
import os
import sys
import time
import os
from locateAllOnScreen import *

import importlib
importlib.reload(pyautogui)

'''
im1 = pyautogui.screenshot()
im1.save('my_screenshot.png')
'''


'''
# used to test the locations I got
locations = list(locateAllOnScreen('button_add_friend_test2.png',  grayscale=False))
print(locations)
print(len(set(locations)))
'''

# click every button on the page and then scroll
# need to know how much I can scroll down

while(True):
    for location in locateAllOnScreen('screenshots/button_add_friend_test.png', grayscale=False):
        print(location)
        button_x, button_y, _, _ = location#pyautogui.center(location)
        pyautogui.moveTo(button_x, button_y, duration=.1)
        pyautogui.click(button_x, button_y)
    break
    pyautogui.scroll(-screenHeight)


