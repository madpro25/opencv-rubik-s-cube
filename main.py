import cv2 as cv
import numpy as np
import os

colours = {1: "red", 2: "white", 3: "green",
           4: "yellow", 5: "orange", 6: "blue"}

discre = open("discrepancies", "w")

directory = "/home/aaditya/roboism-python/rubik/inputs"
for file in os.listdir(directory):

    im = cv.imread("inputs/"+str(file))
    im = cv.resize(im, (0, 0), fx=0.5, fy=0.5)
    hsv = cv.cvtColor(im, cv.COLOR_BGR2HSV)

    # canny = cv.Canny(im, 88, 258)

    # cont, _ = cv.findContours(
    #    canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(im, cont, -1, (0, 255, 0), 3)

    # cv.imshow("canny", canny)
    #                  lh  ls  lv   uh   us   uv
    bounds = np.array([[169, 88, 56, 255, 255, 255],  # 0,112,142,5,244,255
                       [0,  0, 65, 255,  94, 255],
                       [42, 88, 56, 95, 255, 255],
                       [21, 88, 56,  46, 255, 255],
                       [6, 130, 160,  23, 255, 255],
                       [83, 65, 56, 163, 255, 255]])

    masks = [cv.inRange(hsv, bounds[i][:3], bounds[i][3:]) for i in range(6)]

    red = green = yellow = orange = blue = white = np.zeros(im.shape[0])

    red = cv.bitwise_and(im, im, mask=cv.bitwise_or(
        masks[0], cv.inRange(hsv, (0, 112, 142), (5, 244, 255))))
    white = cv.bitwise_and(im, im, mask=masks[1])
    green = cv.bitwise_and(im, im, mask=masks[2])
    yellow = cv.bitwise_and(im, im, mask=masks[3])
    orange = cv.bitwise_and(im, im, mask=masks[4])
    blue = cv.bitwise_and(im, im, mask=masks[5])

    cv.imshow("red", red)
    cv.imshow("green", green)
    cv.imshow("yellow", yellow)
    cv.imshow("orange", orange)
    cv.imshow("blue",  blue)
    cv.imshow("white", white)
    cv.imshow("og", im)

    # for i in range(6):
    #   cv.imshow(colours[i+1], cv.bitwise_and(im, masks[i]))
#   if cv.waitKey(0) & 0xFF == ord('w'):
#        discre.write(str(file)+"\n")

    cv.destroyAllWindows()

discre.close()
