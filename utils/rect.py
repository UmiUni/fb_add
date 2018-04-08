import numpy as np

class GetRectangles:
    '''
    Get all the rectangles that surrounds islands with a particular color
    '''
    _steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    _map = None
    
    def __init__(self, img, color=(0, 0, 0), tol=(5, 5, 5), channel=3):
        '''
        Convert the original image into a 0, 1 map
        '''
        assert channel == img.shape[2] == len(color) == len(tol)
        self._map = np.ones(img.shape[:2]).astype(np.int16)
        for i in range(channel):
            self._map = (self._map&(img[:,:,i] >= color[i]-tol[i])&(img[:,:,i]<= color[i]+tol[i])).astype(np.int16)
    
    def _getIsland(self, i, j):
        '''
        Get Island
        '''
        assert i>=0 and i<self._map.shape[0]
        assert j>=0 and j<self._map.shape[1]
        Q = [(i, j)]
        island = [[i, j]]
        self._map[i][j] = 0
        while Q:
            i, j = Q.pop(0)
            for di, dj in self._steps:
                i1, j1 = i+di, j+dj
                if i1>=0 and i1<self._map.shape[0] and j1>=0 and j1<self._map.shape[1] and self._map[i1][j1]:
                    Q.append((i1, j1))
                    self._map[i1][j1] = 0
                    island.append([i1, j1])
        return np.array(island)
    
    def getRectangles(self):
        '''
        Get all the rectangles
        '''
        rectangles = []
        for i in range(self._map.shape[0]):
            for j in range(self._map.shape[1]):
                if self._map[i][j]:
                    #print(i,j)
                    island = self._getIsland(i, j)
                    left = island[:, 1].min()
                    right = island[:, 1].max() + 1
                    top = island[:, 0].min()
                    bottom = island[:, 0].max() + 1
                    #print((right-left)*1.0/(top-bottom))
                    if abs((right-left)*1.0/(bottom-top)-4.23) <= .5:
                        rectangles.append([top, bottom, left, right])
        return np.array(rectangles)
        
    def reset(self, img, color=(0, 0, 0), tol=(10, 10, 10), channel=3):
        '''
        reset image
        '''
        assert channel == img.shape[2] == len(color) == len(tol)
        self._map = np.ones(img.shape[:2]).astype(np.int16)
        for i in range(channel):
            self._map = (self._map&(img[:,:,i] >= color[i]-tol[i])&(img[:,:,i]<= color[i]+tol[i])).astype(np.int16)