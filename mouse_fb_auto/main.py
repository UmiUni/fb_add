import pyautogui
import os
import sys
import time
import os
from locateAllOnScreen import *

import importlib
importlib.reload(pyautogui)

im1 = pyautogui.screenshot()
im1.save('my_screenshot.png')

locations = list(locateAllOnScreen('button_add_friend_test3.png',  grayscale=False))
print(locations)
print(len(set(locations)))

'''
while(True):
    for location in locateAllOnScreen('button_add_friend_test3.png', grayscale=True):
        #print(location)
        button_x, button_y, _, _ = location#pyautogui.center(location)
        pyautogui.moveTo(button_x, button_y, duration=1)
    break
    pyautogui.scroll(-screenHeight)
'''
