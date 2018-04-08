import numpy as np
#from skimage.transform import resize
import scipy.misc
from PIL import Image

class SimpleIdentifier:
    ''' Determine weither rectangles are "add friend" '''
    _refs = None
    _height = None
    _width = None
    _max_height = None
    _min_height = None
    _max_width = None
    _min_width = None
    
    def __init__(self, references, height=32, width=256, maxh=50, minh=20, maxw=200, minw=80):
        self._height = height
        self._width = width
        self._max_height = maxh
        self._min_height = minh
        self._max_width = maxw
        self._min_width = minw
        self._refs = []
        for ref in references:
            self._refs.append(scipy.misc.imresize(ref, (height, width)))
    
    def _isTarget(self, crop, threshold):
        '''
        Determine whether a rectangle is a "add friend" button
        '''
        crop = scipy.misc.imresize(crop, (self._height, self._width))
        min_diff = 10**8
        for ref in self._refs:
            #diff = (crop-ref).reshape(self._height * self._width * 3)
            diff = (crop-ref).flatten()
            min_diff = min(min_diff, np.dot(diff, diff))
        print("in identifier: " + str(min_diff))
        if min_diff <= threshold:
            #print("in identifier: " + str(np.dot(diff, diff)))
            return True
        return False
    
    def getTargetPositions(self, img, rects):
        '''
        Get all the center coordinates of target buttons
        '''
        target_positions = []
        for top, bottom, left, right in rects:
            if (bottom - top < self._min_height) or (bottom - top > self._max_height):
                continue
            if (right-left < self._min_width) or (right-left > self._max_width):
                continue
            target_positions.append([top, bottom, left, right])
        return target_positions

        # min_diff = 10 ** 8
        # diffs = []
        # for i, (top, bottom, left, right) in enumerate(rects):
        #     crop = img[top: bottom, left: right]
        #     Image.fromarray(crop).save('add_friend_button/test_' + str(i) + '.png', "PNG")
        #     crop = scipy.misc.imresize(crop, (self._height, self._width))
        #     cur_min_diff = 10 ** 8
        #     for ref in self._refs:
        #         diff = (crop - ref).flatten()
        #         cur_min_diff = min(cur_min_diff, np.dot(diff, diff))
        #     diffs.append(cur_min_diff)
        #     min_diff = min(cur_min_diff, min_diff)
        #
        # print(diffs)
        # target_positions = []
        # for (top, bottom, left, right), diff in zip(rects, diffs):
        #     if (bottom-top < self._min_height) or (bottom-top > self._max_height):
        #         continue
        #     if (right-left < self._min_width) or (right-left > self._max_width):
        #         continue
        #     if (diff == min_diff):
        #         target_positions.append([int((top + bottom) / 2), int((left + right) / 2)])
        # return target_positions

        # for i, (top, bottom, left, right) in enumerate(rects):
        #     if (bottom-top < self._min_height) or (bottom-top > self._max_height):
        #         continue
        #     if (right-left < self._min_width) or (right-left > self._max_width):
        #         continue
        #     crop = img[top: bottom, left: right]
        #     # Image.fromarray(crop).save('add_friend_button/frank_'+str(i)+'.png', "PNG")
        #     if self._isTarget(crop, threshold):
        #         target_positions.append([int((top+bottom)/2), int((left+right)/2)])
        #     # target_positions.append([int((top + bottom) / 2), int((left + right) / 2)])
