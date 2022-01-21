from turtle import heading
import cv2
from matplotlib import widgets
import numpy as np

img = cv2.imread('../Resources/cards.jpg')

# Defining points from img
pts1 = np.float32([
    [111, 219], [287, 188],
    [154, 482], [352, 440],
])

# Setting custom dimensions
width, height = 250, 350

# Specifying point locations
pts2 = np.float32([
    [0, 0], [width, 0],
    [0, height], [width, height],
])

# Getting the perspective matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Getting warp-output for img
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Image', img)
cv2.imshow('Image-Output', imgOutput)
cv2.waitKey(0)
