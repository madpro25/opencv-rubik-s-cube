import cv2 as cv
import numpy as np
import os

colours = {1: "red", 2: "white", 3: "green",
           4: "yellow", 5: "orange", 6: "blue"}

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
    bounds = np.array([[169, 88, 100, 255, 255, 255],
                       [0,  0, 65, 255,  94, 255],
                       [68, 88, 100, 95, 255, 255],
                       [21, 88, 100,  70, 255, 255],
                       [4, 88, 100,  28, 255, 255],
                       [86, 88, 100, 122, 255, 255]])

    masks = [cv.inRange(hsv, bounds[i][:3], bounds[i][3:]) for i in range(6)]

    red = green = yellow = orange = blue = white = np.zeros(im.shape[0])

    red = cv.bitwise_and(im, im, mask=masks[0])
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
    cv.waitKey(0)

    cv.destroyAllWindows()
