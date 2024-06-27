import cv2 as cv
import numpy as np


def reacting_objects(display):
    object1 = cv.imread(r'/cv_tamples/box without a coin.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(display, object1, cv.TM_SQDIFF_NORMED)
    threshold = 0.85
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    if locations:
        object_w = object1.shape[1]
        object_h = object1.shape[0]
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        for loc in locations:
            top_left = loc
            bottom_right = (top_left[0] + object_w, top_left[1] + object_h)
            cv.rectangle(display, top_left, bottom_right, line_color, line_type)
    cv.imshow('Matches', display)
