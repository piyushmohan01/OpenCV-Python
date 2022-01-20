# import cv2
# img = cv2.imread("../Resources/lena.png")      # Read image and store
# cv2.imshow("Output", img)                   # show image in window
# cv2.waitKey(0)                              # provide delay (0-inf)

# ------------------------------------------------------------------ #

# import cv2
# cap = cv2.VideoCapture("../Resources/test_video.mp4")

# while True:
#     success, img  = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

# ------------------------------------------------------------------ #

import cv2
cap = cv2.VideoCapture(0)
cap.set(3, 640)                 # setting width
cap.set(4, 480)                 # setting height
cap.set(10, 100)                # setting brightness

while True:
    success, img  = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
