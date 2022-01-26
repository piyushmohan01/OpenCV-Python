import cv2
import numpy as np

# ------------------------------------------------------------------ #

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], \
                        imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y]= cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], \
                    imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

# ------------------------------------------------------------------ #

def getContours(img):
    """
    1) Find contours
    2) For each contour, find the area
    3) Draw the contours on the image
    4) Find the perimeter for each contour
    5) Use the perimeter to find edges of shapes
    6) Find the number of edges from array length
    7) Get co-ordinates and measures for BoundingRect
    8) Define the objectType wrt the number of edges
    9) Differentiate between squares and rectangles 
    10) Draw the BoundingRect along with objectType
    """
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # findContours(imgName, retrievalMethod, approximation)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:                      # 500 in pixels
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # drawContours(imgToDrawOn, contour, contourIndex, BGRcolor, thickness)
            perimeter = cv2.arcLength(cnt, True)
            # arcLength(contourName, isClosed)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            # approxPolyDP(contourName, resolution, isClosed)
            print(len(approx))
            objCorner = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCorner == 3: objectType = 'Tri'
            elif objCorner == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio <1.05: objectType = 'Square'
                else: objectType ='Rect'
            elif objCorner > 4: objectType = 'Circle'
            else: objectType = 'None'
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType, (x+(w//2)-10, y+(h//2)-10),
            cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
            # Finding objectType and displaying near the center


# ------------------------------------------------------------------ #

img = cv2.imread('../Resources/shapes.png')
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgBlank = np.zeros_like(img)

getContours(imgCanny)                       # Call getContours()

imgStack = stackImages(0.5, (
        [img, imgGray, imgBlur],
        [imgCanny, imgContour, imgBlank]
    )
)

cv2.imshow('Stack', imgStack)
cv2.waitKey(0)
