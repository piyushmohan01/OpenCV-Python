import cv2
import numpy as np

# img = np.zeros((512, 512))              # Black Image - Size 512x512
img = np.zeros((512, 512, 3), np.uint8) # Coloured Image - Size 512x512

# img[:] = 255, 0, 0                      # Setting Blue-BGR for entire img
# img[200:300, 100:300] = 255, 0, 0       # Setting Blue-BGR for smaller portion

# ------------------------------------------------------------------ #

# cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)
# line(imageName, startPt, endPt, BGRcolor, thickness)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# img.shape --> 512 x 512 x 3
# img.shape[1] --> width
# img.shape[0] --> height
# Line till the edge of the image (512, 512)

# ------------------------------------------------------------------ #

cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
# rectangle(imageName, startPt, endPt, BGRcolor, thickness)

# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)
# cv2.FILLED instead of thickness to fill the rectangle

# ------------------------------------------------------------------ #

cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
# circle(imageName, centrePt, radius, BGRcolor, thickness)

# ------------------------------------------------------------------ #

cv2.putText(img, "OPEN-CV", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 2)
# putText(imageName, text, startPt, textFont, scale, BGRcolor, thickness)

# ------------------------------------------------------------------ #

cv2.imshow('Image', img)
cv2.waitKey(0)
