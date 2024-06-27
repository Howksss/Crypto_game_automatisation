import cv2 as cv
import time as t
from time import time

from vision import reacting_objects
from windowcapture import WindowCapture

wincap = WindowCapture(None)


loop_time = time()
while True:
    screenshot = wincap.get_screenshot()
    reacting_objects(screenshot)
    cv.imshow('Computer vision', screenshot)
    print(f'FPS {1 / (time() - loop_time)}')
    loop_time = time()
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
