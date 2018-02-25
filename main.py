import pyautogui
import os
import sys
import time
import numpy as np
from utils.rect import GetRectangles
from utils.identifier import SimpleIdentifier
from PIL import Image
from PIL import ImageOps

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
needleImage = 'screenshots/button_add_friend_test.png'
needleFileObj = None
if isinstance(needleImage, str):
	# 'image' is a filename, load the Image object
	needleFileObj = open(needleImage, 'rb')
	needleImage = Image.open(needleFileObj)
# convert to numpy array and remove alpha
needleImage = np.array(needleImage)[:,:,:3]
SimpleIdentifier = SimpleIdentifier([needleImage])

while(True):
	haystackImage = pyautogui.screenshot()
	haystackFileObj = None
	if isinstance(haystackImage, str):
		# 'image' is a filename, load the Image object
		haystackFileObj = open(haystackImage, 'rb')
		haystackImage = Image.open(haystackFileObj)
	haystackImage = np.array(haystackImage)[:,:,:3]
	
	getRect = GetRectangles(haystackImage, tuple(needleImage[0,0]))
	rects = getRect.getRectangles()
	target_rects = SimpleIdentifier.getTargetPositions(haystackImage, rects, 5*10**7)
	print (target_rects)

	for location in target_rects:
		#print(location)
		button_x, button_y = location#pyautogui.center(location)
		pyautogui.moveTo(button_y/2, button_x/2, duration=.5)
		#pyautogui.click(button_x, button_y)
	break
	pyautogui.scroll(-screenHeight)


