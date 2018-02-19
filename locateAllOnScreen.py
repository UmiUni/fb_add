def getRgbRange(pixel, off=10):
	return [range(channel - off, channel + off) for channel in pixel[:-2]]

def inRgbRange(pixel, rgb_range):
	if isinstance(pixel, list):
		# test every channel
		for p, r in zip(pixel, rgb_range):
			if p not in r:
				return False
		return True
	else:
		if pixel not in rgb_range:
			return False
		return True

# general util to test if two rectangles are similar
def isSimilar(rect1, rect2):
	pass

def search(x, y, haystackImageData, haystackImage, needleImage, rgb_range, candidate, ret, visited):
	haystackWidth, haystackHeight = haystackImage.size
	#你还是要找矩形
	if x >= haystackWidth or y >= haystackHeight or visited[y][x]:
		#print('bc')
		#print (visited[y][x])
		#print (y, x)
		return

	if not inRgbRange(haystackImageData[x, y], rgb_range):
		#print (y,x)
		#print ('wow')
		visited[y][x] = True
		return

	visited[y][x] = True
	#print (y,x)
	if (x+1 >= haystackWidth or not inRgbRange(haystackImageData[x+1, y], rgb_range)) \
		and (y+1 >= haystackHeight or not inRgbRange(haystackImageData[x, y+1], rgb_range)):
		#print (y,x)
		candidate.append(x); candidate.append(y)
		if isSimilar(haystackImage.crop(tuple(candidate)), needleImage):
			ret.append(candidate)
		return

	search(x+1, y, haystackImageData, haystackWidth, haystackHeight, needleImage, rgb_range, candidate, ret, visited)
	#print('after first recursion')
	#print (y,x)
	search(x, y+1, haystackImageData, haystackWidth, haystackHeight, needleImage, rgb_range, candidate, ret, visited)
	#print('after 2nd recursion')
	#print (y,x)

	return


def locateAll(needleImage, haystackImage, grayscale=False, limit=None):
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

	if grayscale:
		needleImage = ImageOps.grayscale(needleImage)
		haystackImage = ImageOps.grayscale(haystackImage)

	needleWidth, needleHeight = needleImage.size
	haystackWidth, haystackHeight = haystackImage.size
	needleImageData = needleImage.load()
	haystackImageData = haystackImage.load()


	numMatchesFound = 0
	rgb_range = getRgbRange(needleImageData[0,0])
	print (r_range, g_range, b_range)


	print("start searching")
	button_list = []
	visited = [[False for i in range(haystackWidth)] for j in range(haystackHeight)]
	for y in range(haystackHeight):
		for x in range(haystackWidth):
			if (not visited[y][x]) and inRgbRange(haystackImageData[x, y], rgb_range):
				search(x, y, haystackImage, haystackHeight, needleImage, rgb_range, [x,y], button_list, visited)
			else:
				visited[y][x] = True

	print (button_list)

def locateAllOnScreen(image, grayscale=False, limit=None, region=None):
    screenshotIm = pyautogui.screenshot(region=region)
    retVal = locateAll(image, screenshotIm, grayscale, limit)
    if 'fp' in dir(screenshotIm) and screenshotIm.fp is not None:
        screenshotIm.fp.close() # Screenshots on Windows won't have an fp since they came from ImageGrab, not a file.
    return retVal