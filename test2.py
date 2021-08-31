import cv2 as cv
import numpy as np
import os


def cordi(image):
    global X, Y, W, H
    gray = image
    edged = cv.Canny(gray, 50, 200)
    contours, _ = cv.findContours(
        edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.imshow("canny", edged)
    try:
        # Sort by left to right using our x_cord_contour function
        contours_left_to_right = sorted(
            contours, key=cv.contourArea, reverse=True)
        x, y, w, h = cv.boundingRect(contours_left_to_right[0])
        X, Y, W, H = x, y, w, h
        return x, y, w, h, contours
    except:
        return X, Y, W, H, contours


def box(frame, i):
    maskg = masks[i]
    maskg = cv.medianBlur(maskg, 5)
    x, y, w, h, contours = cordi(maskg)
    result = cv.rectangle(frame.copy(), (x, y), (x+w, y+h), (0, 0, 255), 2)
    return result, maskg, contours


colours = {1: "red", 2: "white", 3: "green",
           4: "yellow", 5: "orange", 6: "blue"}

discre = open("discrepancies", "w")

directory = "/home/aaditya/roboism-python/rubik/inputs"
for file in os.listdir(directory):

    im = cv.imread("inputs/"+str(file))
    im = cv.resize(im, (0, 0), fx=0.5, fy=0.5)
    hsv = cv.cvtColor(im, cv.COLOR_BGR2HSV)
    hsv = cv.erode(hsv, None, iterations=2)
    hsv = cv.dilate(hsv, None, iterations=2)

    # canny = cv.Canny(im, 88, 258)

    # cont, _ = cv.findContours(
    #    canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(im, cont, -1, (0, 255, 0), 3)

    # cv.imshow("canny", canny)
    #                  lh  ls  lv   uh   us   uv
    bounds = np.array([[169, 88, 56, 255, 255, 255],  # red 0,112,142,5,244,255
                       [0,  0, 65, 255,  94, 255],  # white
                       [42, 88, 56, 95, 255, 255],  # green
                       [21, 88, 56,  46, 255, 255],  # yellow
                       [6, 130, 160,  23, 255, 255],  # orange
                       [83, 65, 56, 163, 255, 255]])  # blue

    masks = [cv.inRange(hsv, bounds[i][:3], bounds[i][3:]) for i in range(6)]

    red = green = yellow = orange = blue = white = np.zeros(im.shape[0])
    masks[0] = cv.bitwise_or(
        masks[0], cv.inRange(hsv, (0, 112, 142), (5, 244, 255)))

    red = cv.bitwise_and(im, im, mask=masks[0])
    white = cv.bitwise_and(im, im, mask=masks[1])
    green = cv.bitwise_and(im, im, mask=masks[2])
    yellow = cv.bitwise_and(im, im, mask=masks[3])
    orange = cv.bitwise_and(im, im, mask=masks[4])
    blue = cv.bitwise_and(im, im, mask=masks[5])

    result, _, contours = box(im, 0)
    cv.drawContours(im, contours, -1, (0, 255, 0), 3)

    cv.imshow("red", red)
    cv.imshow("green", green)
    cv.imshow("yellow", yellow)
    cv.imshow("orange", orange)
    cv.imshow("blue",  blue)
    cv.imshow("white", white)
    cv.imshow("og", im)
    cv.imshow("Box", result)
    # for i in range(6):
    #   cv.imshow(colours[i+1], cv.bitwise_and(im, masks[i]))
    if cv.waitKey(0) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        exit()

    cv.destroyAllWindows()

discre.close()
exit()