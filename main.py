import cv2 as cv
import numpy as np

colours = {1: "red", 2: "white", 3: "green",
           4: "yellow", 5: "orange", 6: "blue"}

im = cv.imread("inputs/WhatsApp Image 2021-02-16 at 7.58.40 PM.jpeg")
im = cv.resize(im, (480, 480))
hsv = cv.cvtColor(im, cv.COLOR_BGR2HSV)

# canny = cv.Canny(im, 88, 258)

# cont, _ = cv.findContours(
#    canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# cv.drawContours(im, cont, -1, (0, 255, 0), 3)

# cv.imshow("canny", canny)
#                  lh  ls  lv   uh   us   uv
bounds = np.array([[0, 40, 50,   6, 100, 100],
                   [0,  0, 65, 359,  40, 100],
                   [84, 40, 50, 152, 100, 100],
                   [55, 40, 50,  70, 100, 100],
                   [20, 40, 50,  37, 100, 100],
                   [200, 40, 50, 269, 100, 100]])

masks = [cv.inRange(hsv, bounds[i][:3], bounds[i][3:]) for i in range(6)]
cv.imshow("test", masks[3])
cv.imshow("image", hsv)
# for i in range(6):
#   cv.imshow(colours[i+1], cv.bitwise_and(im, masks[i]))
cv.waitKey(0)

cv.destroyAllWindows()
