import pyautogui
import os
import sys
import time
import numpy as np
from utils.rect import GetRectangles
from utils.identifier import SimpleIdentifier
from utils.misc import *
from PIL import Image
#import win32clipboard

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

#needleImage = 'add_friend_button/win_chrome_120.PNG'	#button_add_friend_test2

needleImageDir = 'add_friend_button'
ref = []
for f in os.listdir(needleImageDir):
	needleImage = needleImageDir+'/'+f
	needleFileObj = None
	if isinstance(needleImage, str):
		# 'image' is a filename, load the Image object
		needleFileObj = open(needleImage, 'rb')
		needleImage = Image.open(needleFileObj)
		#needleImage.show()
	# convert to numpy array and remove alpha
	needleImage = np.array(needleImage)[:,:,:3]
	ref.append(needleImage)
SimpleIdentifier = SimpleIdentifier(ref, needleImage.shape[0], needleImage.shape[1])

while(True):
	haystackImage = pyautogui.screenshot()
	haystackFileObj = None
	if isinstance(haystackImage, str):
		# 'image' is a filename, load the Image object
		haystackFileObj = open(haystackImage, 'rb')
		haystackImage = Image.open(haystackFileObj)
	haystackImage = np.array(haystackImage)[:,:,:3]

	#print ( tuple(needleImage[0,0]))	#(66, 103, 178)
	fbBlue = tuple(needleImage[2,2])
	#fbBlue = (66, 103, 178)
	print(fbBlue)
	getRect = GetRectangles(haystackImage, fbBlue)
	rects = getRect.getRectangles()
	target_rects = SimpleIdentifier.getTargetPositions(haystackImage, rects)
	print (target_rects)

	ctr = 0
	for location in target_rects:
		#print(location)
		button_x, button_y = location#pyautogui.center(location)
		pyautogui.moveTo(button_y, button_x, duration=.5)
		#pyautogui.click(button_y/2, button_x/2)	#for mac
		try:
			pyautogui.moveTo(button_y-250, button_x-60, duration=.5)
		# 	nameBox = haystackImage[button_x-60 : button_x+60, button_y-250 : button_y-20]
		# except ValueError:
		# 	continue
		#Image.fromarray(nameBox).show()#save('name_box/'+str(ctr)+'.png', "PNG") #show()
		# try:
		# 	isChinese = ocr(nameBox)
		except ValueError:
			continue
		# if (isChinese):
			#pyautogui.moveTo(findFirstBlue(nameBox, button_x-60, button_y-250, fbBlue)[::-1], duration=.5)
			# pyautogui.click(button='right')
			# for i in range (5):
			# 	pyautogui.press('down')
			# pyautogui.press('enter')
			# win32clipboard.OpenClipboard()
			# data = win32clipboard.GetClipboardData()
			# win32clipboard.CloseClipboard()
			# print (data)
			# pass
			#pyautogui.click(button_y, button_x)	#for mac
		ctr += 1
	break
	#pyautogui.scroll(-1100)


