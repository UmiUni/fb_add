import pyautogui
import os
import sys
import time
import numpy as np
from utils.rect import GetRectangles
from utils.identifier import SimpleIdentifier
from utils.misc import *
from PIL import Image
# pip install win32clipboard
import win32clipboard
from collections import deque
import random
from utils import gui_bot

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

# needleImage = 'add_friend_button/win_chrome_120.PNG'	#button_add_friend_test2

time.sleep(3)

needleImageDir = 'add_friend_button'
ref = []
for f in os.listdir(needleImageDir):
    needleImage = needleImageDir + '/' + f
    needleFileObj = None
    if isinstance(needleImage, str):
        # 'image' is a filename, load the Image object
        needleFileObj = open(needleImage, 'rb')
        needleImage = Image.open(needleFileObj)
    # needleImage.show()
    # convert to numpy array and remove alpha
    needleImage = np.array(needleImage)[:, :, :3]
    ref.append(needleImage)
SimpleIdentifier = SimpleIdentifier(ref, needleImage.shape[0], needleImage.shape[1])

friendIdQ = deque()
friendIdQ.append('superchaoran')  # 'https://www.facebook.com/superchaoran/friends'
for depth in range(3):
    while (len(friendIdQ) != 0):
        curPage = 'https://www.facebook.com/' + friendIdQ.popleft() + '/friends'
        print(curPage)
        pyautogui.hotkey('ctrl', 'l')
        # print (list(curPage))
        pyautogui.press(list(curPage))
        time.sleep(random.uniform(0.5, 2))
        pyautogui.press('enter')
        time.sleep(random.uniform(1.5, 4))

        noFriendFoundCtr = 0
        while (noFriendFoundCtr < 5):
            haystackImage = pyautogui.screenshot()
            print(haystackImage.size)
            haystackFileObj = None
            if isinstance(haystackImage, str):
                # 'image' is a filename, load the Image object
                haystackFileObj = open(haystackImage, 'rb')
                haystackImage = Image.open(haystackFileObj)
            haystackImage = np.array(haystackImage)[:, :, :3]

            # print ( tuple(needleImage[0,0]))	#(66, 103, 178)
            fbBlue_addButton = tuple(needleImage[2, 2])
            # fbBlue = (66, 103, 178)
            # print(fbBlue_addButton)
            fbBlue_nameBox = (54, 88, 153);
            getRect = GetRectangles(haystackImage, fbBlue_addButton)
            rects = getRect.getRectangles()
            target_rects = SimpleIdentifier.getTargetPositions(haystackImage, rects)
            print(target_rects)

            # ctr = 0
            noFriendFound = True
            for target_rect in target_rects:
                # print(location)
                button_x, button_y = getCenter(target_rect)  # pyautogui.center(location)
                gui_bot.random_move_to(button_x, button_y)

                try:
                    top, bottom, left, right = target_rect
                    height, width = getDim(target_rect)
                    # move to add friend button top left corner
                    nameBoxRight = int(button_x - width / 2)
                    nameBoxLeft = int(nameBoxRight - width * 1.8)
                    nameBoxTop = int(button_y - height / 2 - height * 1.5)
                    nameBoxButtom = int(button_y + height / 2 + height * 1.5)
                    nameBox = haystackImage[nameBoxTop: nameBoxButtom, nameBoxLeft: nameBoxRight]
                except ValueError:
                    continue
                Image.fromarray(nameBox)  # .show()#save('name_box/'+str(ctr)+'.png', "PNG") #show()
                try:
                    isChinese = ocr(nameBox)
                except ValueError:
                    continue
                if (isChinese):
                    print("yes")
                    name_x, name_y = findFirstBlue(nameBox, nameBoxLeft, nameBoxTop, fbBlue_nameBox)
                    gui_bot.random_move_to(name_x, name_y)
                    # copy link
                    pyautogui.click(button='right')
                    for i in range(5):
                        pyautogui.press('down')
                    pyautogui.press('enter')
                    # read from clipboard and process
                    win32clipboard.OpenClipboard()
                    data = win32clipboard.GetClipboardData()
                    win32clipboard.CloseClipboard()
                    friend_id = (data.split('?')[0]).split('/')[-1]
                    # print (friend_id)
                    # add to queue
                    friendIdQ.append(friend_id)
                    #pyautogui.click(button_y, button_x)
                noFriendFound = False
            # ctr += 1
            # break
            if (noFriendFound == True):
                noFriendFoundCtr += 1
            del haystackImage
            del getRect
            del rects
            del target_rects
            pyautogui.scroll(random.randrange(-1500, -500))
            time.sleep(random.uniform(0.5, 2))
