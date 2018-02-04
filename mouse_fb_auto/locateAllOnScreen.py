import pyautogui
from scipy import spatial
from PIL import Image
from PIL import ImageOps

def _kmp(needle, haystack): # Knuth-Morris-Pratt search algorithm implementation (to be used by screen capture)
    # build table of shift amounts
    shifts = [1] * (len(needle) + 1)
    shift = 1
    for pos in range(len(needle)):
        while shift <= pos and needle[pos] != needle[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in haystack:
        while matchLen == len(needle) or \
              matchLen >= 0 and needle[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(needle):
            yield startPos

def locateAll_(needleImage, haystackImage, grayscale=False, limit=None):
    needleFileObj = None
    haystackFileObj = None
    if isinstance(needleImage, str):
        # 'image' is a filename, load the Image object
        needleFileObj = open(needleImage, 'rb')
        needleImage = Image.open(needleFileObj)
    if isinstance(haystackImage, str):
        # 'image' is a filename, load the Image object
        haystackFileObj = open(haystackImage, 'rb')
        haystackImage = Image.open(haystackFileObj)

    needleImage = None
    haystackImage = None
    if grayscale:
        needleImage = ImageOps.grayscale(needleImage)
        haystackImage = ImageOps.grayscale(haystackImage)

    needleWidth, needleHeight = needleImage.size
    haystackWidth, haystackHeight = haystackImage.size
    print(needleWidth, needleHeight)
    print(haystackWidth, haystackHeight)
    needleImageData = tuple(needleImage.getdata()) # TODO - rename to needleImageData??
    haystackImageData = tuple(haystackImage.getdata())

    needleImageRows = [needleImageData[y * needleWidth:(y+1) * needleWidth] for y in range(needleHeight)] # LEFT OFF - check this
    needleImageFirstRow = needleImageRows[0]

    assert len(needleImageFirstRow) == needleWidth
    assert [len(row) for row in needleImageRows] == [needleWidth] * needleHeight

    numMatchesFound = 0
    print("start searching")
    for y in range(haystackHeight):
        #for matchx in range(haystackWidth):
        for matchx in _kmp(needleImageFirstRow, haystackImageData[y * haystackWidth:(y+1) * haystackWidth]):
            foundMatch = True
            # then test row by row
            sim = 0
            for searchy in range(1, needleHeight):
                haystackStart = (searchy + y) * haystackWidth + matchx
                curNeedleImageRow = needleImageData[searchy * needleWidth:(searchy + 1) * needleWidth]
                curHaystackImageRow = haystackImageData[haystackStart:haystackStart + needleWidth]

                '''
                if curNeedleImageRow != curHaystackImageRow:
                    foundMatch = False
                    break
                '''
                #print (len(curNeedleImageRow))
                #print(len(curHaystackImageRow))
                try:
                    sim += 1 - spatial.distance.cosine(curNeedleImageRow, curHaystackImageRow)
                except ValueError:
                    print (len(curHaystackImageRow))

            if (sim / (needleHeight - 1) < .8):
                foundMatch = False

            if foundMatch:
                # Match found, report the x, y, width, height of where the matching region is in haystack.
                numMatchesFound += 1
                yield (matchx, y, needleWidth, needleHeight)
                if limit is not None and numMatchesFound >= limit:
                    # Limit has been reached. Close file handles.
                    if needleFileObj is not None:
                        needleFileObj.close()
                    if haystackFileObj is not None:
                        haystackFileObj.close()


    # There was no limit or the limit wasn't reached, but close the file handles anyway.
    if needleFileObj is not None:
        needleFileObj.close()
    if haystackFileObj is not None:
        haystackFileObj.close()



def locateAllOnScreen(image, grayscale=False, limit=None, region=None):
    screenshotIm = pyautogui.screenshot(region=region)
    retVal = locateAll(image, screenshotIm, grayscale, limit)
    if 'fp' in dir(screenshotIm) and screenshotIm.fp is not None:
        screenshotIm.fp.close() # Screenshots on Windows won't have an fp since they came from ImageGrab, not a file.
    return retVal