from PIL import Image
from PIL import ImageOps
import pyautogui
import time
import numpy as np
from locateAllOnScreen import *
'''
needleImage = "button_add_friend.png"
needleFileObj = open(needleImage, 'rb')
needleImage = Image.open(needleFileObj)
needleWidth, needleHeight = needleImage.size
needleImageData = tuple(needleImage.getdata())
print(needleWidth, needleHeight)
print(len(needleImageData))
'''

# test move
'''
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

# test search
'''
array = numpy.array([[0,0,1,1,0,1], [0,0,1,1,0,1], [0,0,1,1,0,1], [0,0,1,1,0,0]])
haystackImage = Image.fromarray(array)
needleWidth, needleHeight = needleImage.size
haystackImageData = haystackImage.load()
print (haystackImageData[0,0])
'''

'''
# white 255, black 0
pixels = np.array([[0,0,255,255,0,255], [0,0,255,255,0,255], [0,0,255,255,0,255], [0,0,255,255,0,0]])
pixels = pixels.astype('uint8')

# haystackImage = Image.new('L', (6,4))
# haystackImage.putdata(pixels)
# I think this way you need to save onto disk and then read back, although absurd.

haystackImage = Image.fromarray(pixels)
haystackImage.show()

haystackWidth, haystackHeight = haystackImage.size
haystackImageData = haystackImage.load()

rgb_range = range(200,256)	# capture white
button_list = []
# never do this!
# visited = [[False]*haystackWidth]*haystackHeight
visited = [[False for i in range(haystackWidth)] for j in range(haystackHeight)]
for y in range(haystackHeight):
    for x in range(haystackWidth):
        if (not visited[y][x]) and inRgbRange(haystackImageData[x, y], rgb_range):
            candidate = [x,y,0,0]
            search(x, y, haystackImageData, haystackImage, None, rgb_range, candidate, visited)
            button_list.append(candidate)
        else:
            visited[y][x] = True

print (button_list)
'''

# test processBinary 
needleImageFile = 'screenshots/button_add_friend_test.png'
needleFileObj = open(needleImageFile, 'rb')
needleImage = Image.open(needleFileObj)
rgb_range = [range(56, 76), range(93, 113), range(168, 188)] # capture white
processBinary(needleImage, rgb_range)