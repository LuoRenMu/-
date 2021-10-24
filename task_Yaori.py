# -*- codeing = utf-8 -*-
# @Time : 2021/10/10 16:34
# @Author : 罗任姆/LoMu
# @File : task_Yaori.py
# @Software : PyCharm
import pyautogui
import numpy
from config import  *
import aircv as ac
import time
from PIL import ImageGrab
from task import renWumenu

def yaoRi_start(yaoristart):
        x,y=task_accept_pos(yaoristart['result'])
        pyautogui.moveTo(x,y)
        pyautogui.leftClick()
        time.sleep(0.5)
        pyautogui.moveTo(xY_pos(1528, 855))
        pyautogui.leftClick()
        time.sleep(0.5)
        pyautogui.moveTo(xY_pos(801, 686))
        pyautogui.leftClick()
        time.sleep(0.5)
        pyautogui.leftClick()
        time.sleep(0.5)
        pyautogui.press('home')

        task_progress['yaori'] = 1
        renWumenu()
 # 85
def yaoRi_01():
    window_Img = numpy.array(ImageGrab.grab(bbox=(x1_pos,y1_pos,x2_pos,y2_pos)))
    yaoRi_Haojin_Img = numpy.array(ImageGrab.grab(bbox=(68+x1_pos, 630+y1_pos, 384+x1_pos, 737+y1_pos)))
    yaori01_panduan = ac.find_template(window_Img,yaoRi_Haojin_Img)
    if yaori01_panduan != None:
        print()
        print("发现曜日已完成")
        yaoRi_02()
    else:
        print()
        print("曜日开始")
        pyautogui.moveTo(xY_pos(227,482))
        pyautogui.leftClick()
        time.sleep(0.1)
        pyautogui.moveTo(xY_pos(1247, 625))
        pyautogui.leftClick()
        time.sleep(0.1)
        pyautogui.moveTo(xY_pos(802, 683))
        pyautogui.leftClick()
        time.sleep(0.99)
        pyautogui.leftClick()
        time.sleep(0.99)
        pyautogui.press('`')
        print()
        print("曜日活动完成")
def yaoRi_02():
    print()
    print("时空工厂开始")