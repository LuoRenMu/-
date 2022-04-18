# -*- codeing = utf-8 -*-
# @Time : 2021/10/9 12:18
# @Author : 罗任姆/LoMu
# @File : windowRect.py
# @Software : PyCharm
import win32gui
import time
import  numpy
from open3rd_win32 import *
def windowRect(hWnd):
    time.sleep(0.5)
    try:
        rect = win32gui.GetWindowRect(hWnd)  # 获取句柄坐标
    except win32gui.error:
        gameover()
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    return rect
# 输出游戏窗口坐标
def windowRect_show(hWnd):
    time.sleep(0.5)
    try:
        rect = win32gui.GetWindowRect(hWnd) #获取句柄坐标
    except win32gui.error:
        gameover()
    print("窗口坐标",rect)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    print("\t起始Location: (%d, %d)" % (x, y))
    print("\t  窗口Size: (%d, %d)" % (w, h)) #获取窗口大小
    print("Window %s:" % win32gui.GetWindowText(hWnd)) #获取句柄窗口名
    return rect
#测试
def windowNewRect():
    while True:
        i = 0
        try:
            rect = win32gui.GetWindowRect(hWnd)
            if rect!=win32gui.GetWindowRect(hWnd):
                print("%s  坐标发生改变: %s" % (win32gui.GetWindowText(hWnd), win32gui.GetWindowRect(hWnd)))
                i+1
                time.sleep(5)
            elif rect == win32gui.GetWindowRect(hWnd) and i == 1:
                print("%s  坐标发生改变: %s" % (win32gui.GetWindowText(hWnd), win32gui.GetWindowRect(hWnd)))
                time.sleep(5)
            else:continue
        except win32gui.error:
            gameover()

def gameover():
    print("============游戏异常,程序结束!============")
    exit()
