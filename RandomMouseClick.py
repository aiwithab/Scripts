import win32api
import win32con


import random
import time


while True:

    win32api.SetCursorPos((random.randint(200, 400), random.randint(400, 550)))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, random.randint(1, 1000), random.randint(1, 1000), 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, random.randint(1, 1000), random.randint(1, 1000), 0, 0)
    time.sleep(3)
