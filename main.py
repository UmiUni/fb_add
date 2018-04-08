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
	fbBlue_addButton = tuple(needleImage[2, 2])
	#fbBlue = (66, 103, 178)
	print(fbBlue_addButton)
	fbBlue_nameBox = (54,88,153);
	getRect = GetRectangles(haystackImage, fbBlue_addButton)
	rects = getRect.getRectangles()
	target_rects = SimpleIdentifier.getTargetPositions(haystackImage, rects)
	print (target_rects)

	ctr = 0
	for target_rect in target_rects:
		#print(location)
		button_x, button_y = getCenter(target_rect)#pyautogui.center(location)
		pyautogui.moveTo(button_x, button_y, duration=.5)
		#pyautogui.click(button_y/2, button_x/2)	#for mac
		try:
			top, bottom, left, right = target_rect
			height, width = getDim(target_rect)
			# move to add friend button top left corner
			nameBoxRight = int(button_x - width / 2)
			nameBoxLeft = int(nameBoxRight - width * 1.8)
			nameBoxTop = int(button_y - height / 2 - height * 1.5)
			nameBoxButtom = int(button_y + height / 2 + height * 1.5)
			nameBox = haystackImage[nameBoxTop : nameBoxButtom, nameBoxLeft : nameBoxRight]
		except ValueError:
		 	continue
		Image.fromarray(nameBox)#.show()#save('name_box/'+str(ctr)+'.png', "PNG") #show()
		try:
			isChinese = ocr(nameBox)
		except ValueError:
			continue
		if (isChinese):
			print ("yes")
			pyautogui.moveTo(findFirstBlue(nameBox, nameBoxLeft, nameBoxTop, fbBlue_nameBox), duration=.5)
			pyautogui.click(button='right')
			for i in range (5):
				pyautogui.press('down')
			pyautogui.press('enter')
			# win32clipboard.OpenClipboard()
			# data = win32clipboard.GetClipboardData()
			# win32clipboard.CloseClipboard()
			# print (data)
			# pass
			#pyautogui.click(button_y, button_x)	#for mac
		ctr += 1
		break
	break
	#pyautogui.scroll(-1100)


