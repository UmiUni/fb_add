from PIL import Image
from PIL import ImageOps
import pyautogui
import time

'''
needleImage = "button_add_friend.png"
needleFileObj = open(needleImage, 'rb')
needleImage = Image.open(needleFileObj)
needleWidth, needleHeight = needleImage.size
needleImageData = tuple(needleImage.getdata())
print(needleWidth, needleHeight)
print(len(needleImageData))
'''
'''
# test move
print(pyautogui.size())
haystackImage = pyautogui.screenshot()
haystackWidth, haystackHeight = haystackImage.size
print(haystackWidth, haystackHeight)
haystackImage.save('my_screenshot.png')
pyautogui.moveTo(1000, 226, duration=.5)
'''

# test locate pixel on haystack
'''
haystackImage = pyautogui.screenshot()
haystackWidth, haystackHeight = haystackImage.size
#haystackImageData = tuple(haystackImage.getdata())
haystackImageData = haystackImage.load()

for y in range(haystackHeight):
    for x in range(haystackWidth):
        r, g, b = haystackImageData[x,y]
        if b in range(168 , 188) and g in range(93 , 113) and r in range(56 , 76):
            print(x,y)
            pyautogui.moveTo(x,y)
            time.sleep(.2)
            break
#pixel = haystackImageData[510*haystackWidth + 1200]
#print(pixel)
'''

# test locate pixel on needle
'''
needleFileObj = open('screenshots/button_add_friend_test.png', 'rb')
needleImage = Image.open(needleFileObj)
needleWidth, needleHeight = needleImage.size
print(needleImage)
print(needleWidth, needleHeight)
needleImageData = tuple(needleImage.getdata()) 
#pixel = haystackImageData[530 + 1200*haystackHeight]
print(needleImageData)
'''

'''
for l_ in l:
    if l_[1] > 200:
        pyautogui.moveTo(l_[0], l_[1])
'''

# test rgb
'''
im = Image.open('screenshots/fb_blue_Mac.png')
#im = Image.open('screenshots/fb_blue_screenshot.png') #similar result
pix = im.load()
r, g, b, _ = pix[0, 0]
print(r,g,b)
'''
# 66 102 172 so the range thing works

