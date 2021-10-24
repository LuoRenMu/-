# -*- codeing = utf-8 -*-
# @Time : 2021/10/8 22:20
# @Author : YFen4nt0ren
# @File : pil截图.py
# @Software : PyCharm
from PIL import ImageGrab
import win32gui
import time
import numpy
import aircv
import pyautogui
import cv2
hWnd = win32gui.FindWindow("UnityWndClass", None)
rect = win32gui.GetWindowRect(hWnd)
x = rect[0]
y = rect[1]
def imageGrab(a,b,c,d,f=1):
    src = "./3rd_imges/3rd_3_source.png"
    if f == 2:
        img = ImageGrab.grab(bbox=(a + x, b + y, c + x, d + y))
        img.save(src)
        aircv.show(numpy.array(img))
    else:
        img_array=numpy.array((ImageGrab.grab(bbox=(a,b,c,d))))
        cv2.imshow('img',"./3rd_imges/3rd_3_source.png")
        cv2.waitKey()
def a():

    return 1
if __name__ == '__main__':
    win32gui.ShowWindow(hWnd, 6)  # 将窗口最小化
    win32gui.ShowWindow(hWnd, 1)  # 将窗口最大化并激活    如果只调用这个窗口将无法激活
    #time.sleep(1)
   # imageGrab(317,727,452,811,2)
    c,d=(1556,424)   #
    a = (c-x,d-y)
   # pyautogui.moveTo(850 + x, 481 + y)
    #pyautogui.moveTo(a)
    #pyautogui.scroll(-2500)
    print(a)
#649, 776  860, 776   1078, 776    1286, 776    1509, 776