import numpy as np
#from skimage.transform import resize
import scipy.misc

class SimpleIdentifier:
    ''' Determine weither rectangles are "add friend" '''
    _refs = None
    _height = None
    _width = None
    _max_height = None
    _min_height = None
    _max_width = None
    _min_width = None
    
    def __init__(self, references, height=32, width=256, maxh=1E6, minh=0, maxw=1E6, minw=0):
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
        for ref in self._refs:
            #diff = (crop-ref).reshape(self._height * self._width * 3)
            diff = (crop-ref).flatten()
            if np.dot(diff, diff) <= threshold:
                return True
        return False
    
    def getTargetPositions(self, img, rects, threshold=5.):
        '''
        Get all the center coordinates of target buttons
        '''
        target_positions = []
        for top, bottom, left, right in rects:
            if (bottom-top < self._min_height) or (bottom-top > self._max_height):
                continue
            if (right-left < self._min_width) or (right-left > self._max_width):
                continue
            crop = img[top: bottom, left: right]
            if self._isTarget(crop, threshold):
                target_positions.append([int((top+bottom)/2), int((left+right)/2)])
        return target_positions