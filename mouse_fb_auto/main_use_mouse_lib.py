import mouse
import sys
import os
import time
START_X = 380
START_Y = 160
MOVE_TO_FRIEND_X = 440
FRIEND_BLOCK_Y = 440
FRIEND_BLOCK_X = 115 #should float with the width of the add friend button

mouse.move(START_X, START_Y)
time.sleep(1)
mouse.wheel(delta=-3.3)
time.sleep(1)
cur_x = START_X
cur_y = START_Y

mouse.wheel(delta=-3.25)
time.sleep(1)

mouse.wheel(delta=-3.25)
time.sleep(1)

mouse.wheel(delta=-3.25)
time.sleep(1)

mouse.wheel(delta=-3.25)
i = 1
'''
for i in range(8):
    
    mouse.click()
    mouse.move(FRIEND_BLOCK_Y, 0, absolute=False, duration=1)
    mouse.click()
    time.sleep(1)
    cur_x, cur_y = mouse.get_position()
    mouse.move(cur_x - FRIEND_BLOCK_Y, cur_y+FRIEND_BLOCK_X,  duration=1)
'''
#mouse.move(MOVxE_TO_FRIEND_X-START_X, 0, absolute=False, duration=1)
#time.sleep(1)
'''
mouse.click()
mouse.move(0, FRIEND_BLOCK_Y, absolute=False, duration=1)
mouse.click()
'''

#mouse.drag(start_x=START_X)


'''


#mouse.click()
mouse.move(FRIEND_BLOCK_X, 0, absolute=False, duration=2)
'''
print(mouse.get_position())
