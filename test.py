import cv2 as cv
import os

directory = "/home/aaditya/roboism-python/rubik/inputs"
for file in os.listdir(directory):

    im = cv.imread("inputs/"+str(file))
    imor = cv.resize(im, (480, 480))
    im = cv.resize(im, (480, 480))
    #im = cv.cvtColor(im, cv.COLOR_BGR2HSV)
    canny = cv.Canny(im, 78, 258)
    cont, _ = cv.findContours(
        canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    cv.drawContours(im, cont, -1, (0, 255, 0), 3)
    cv.imshow("original", imor)
    cv.imshow("image", im)
    cv.imshow("canny", canny)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print(str(file))
