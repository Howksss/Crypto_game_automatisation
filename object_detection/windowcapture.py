import numpy as np
import pyautogui
import win32con
import win32gui
import win32ui


class WindowCapture:
    w = 0
    h = 0
    cropped_x = 0
    cropped_y = 0
    hwnd = None

    def __init__(self, window_name=None):

        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception(f'Window not found: {window_name}')

        self.w = 1000
        self.h = 1030

    def get_window_names(self):
        windows = pyautogui.getAllWindows()
        for window in windows:
            print(window.title)

    def get_screenshot(self):

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((-200, -200), (self.w, self.h), dcObj, (0, 0), win32con.SRCCOPY)
        dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        return img
