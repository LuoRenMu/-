# -*- codeing = utf-8 -*-
# @Time : 2021/10/7 23:35
# @Author : 罗任姆/LoMu
# @File : open3rd_win32.py
# @Software : PyCharm
import pyautogui
import aircv as ac
import win32api,win32gui
from PIL import ImageGrab
import time
from windowRect import *
import numpy
from config import *
from task_Yaori import *
from task import *
# 截图
def imageGrab(a, b, c, d, img_name, f=1):  # 1位坐标截图   2为窗口坐标定位截图 3为全屏截图
    src = f"./3rd_imges/search/3rd_{img_name}_search.png"
    try:
        rect_imgGrab = win32gui.GetWindowRect(hWnd)
    except win32gui.error:
        gameover()
    x = rect_imgGrab[0]
    y = rect_imgGrab[1]
    if f == 2:
        img = numpy.array(ImageGrab.grab(bbox=(a + x, b + y, c + x, d + y)))
    elif f == 1:
        ImageGrab.grab(bbox=(a, b, c, d)).save(src)
        img = ac.imread(src)
    elif f == 3:
        img = numpy.array(ImageGrab.grab(bbox=rect))
    elif f == 4:
        img = numpy.array(ImageGrab.grab(bbox=(a, b, c, d)))
    return img

def game_Home():
    winDowImg = numpy.array(imageGrab(0,0,0,0,"WindowImg",3))
    game_home_ipt = bool(ac.find_template(winDowImg,game_home_img))
    if  game_home_ipt is True:
        return True
    else:
        return False
# 游戏登陆
def login_game(hWnd):
    try:
        win32gui.GetWindowRect(hWnd)  # 获取句柄坐标
    except win32gui.error:  # 未发现游戏句柄 退出程序
        gameover()
    rect = windowRect(hWnd)
    x1_pos,y1_pos,x2_pos,y2_pos = rect

    # 读取登陆状态
    imageGrab(x1_pos, y1_pos, x2_pos, y2_pos, "Window_Game", 1)  # 截全屏保存
    img_array = imageGrab(0, 0, 0, 0, "Window_Game", 3)  # 截全屏numpy
    xieyi_img_array = imageGrab(425, 133, 1180, 810, "xieyi", 2)  # 用户协议
    login_press_imgsrc = imageGrab(643, 820, 957, 883, "login_press", 2)  # 用户登陆
    login_press = (ac.find_template(login_press_imgsrc,login_press_img_source, 0.8))
    login_xieyi = (ac.find_template( xieyi_img_array,login_xieyi_img_source))
    login_press_click = (ac.find_template(img_array,login_press_click_source, 0.9))
    login_wangluo = (ac.find_template(img_array,login_exit_img,  0.8))
    # zhucaidan = (ac.find_template(zhucaidan_img,img_array))
    img_array_panduan = imageGrab(x1_pos, y2_pos - 100, x1_pos + 1024, y2_pos, "Window_Game", 4)  # 截全屏numpy
    gameing_panduan = ac.find_template(img_array_panduan,gameing_panduan_img)
    gongGao_ipt = ac.find_template(renWumenu_img, img_array)
    # print(login_xieyi) #{'result': (377.5, 338.5), 'rectangle': ((0, 0), (0, 677), (755, 0), (755, 677)), 'confidence': 0.5045602321624756}

    # 检测
    if login_wangluo != None:
        print("=====游戏发生:网络连接失败 尝试重试=====")
        pyautogui.moveTo((586 + x1_pos, 663 + y1_pos))
        pyautogui.leftClick()
    elif login_press != None:
        print("===请登录===")
        time.sleep(1)
    elif login_xieyi != None:
        img_array = imageGrab(0, 0, 0, 0, "Window_Game", 3)
        xieyi_press_points = ac.find_template(img_array,login_xieyi_press_source)['result']
        pyautogui.moveTo(xieyi_press_points+(x1_pos,y1_pos))
        time.sleep(1)
        pyautogui.leftClick()
        print("已接受用户协议")
    elif login_press_click != None:
        pyautogui.moveTo(x2_pos / 2, y2_pos / 2)
        time.sleep(1)
        pyautogui.leftClick()
        pyautogui.leftClick()
        pyautogui.leftClick()
        print()
        print("账户已登录")
        print()
    if bool(ac.find_template(imageGrab(0, 0, 0, 0, "Window_Game", 3),login_press_click_source, 0.8)):
        return True
    if gameing_panduan != None:
        pyautogui.keyDown("home")
        pyautogui.keyUp('home')
        return True
    elif game_Home() is True :
        return True
    if gongGao_ipt != None:
        return True
    else:
        return False

def gonggao():
    rect = windowRect(hWnd)
    x1_pos, y1_pos, x2_pos, y2_pos = rect
    gonggao_pos = (1492 + x1_pos, 130 + y1_pos)
    img_array = imageGrab(0, 0, 0, 0, "Window_Game", 3)
    gongGao_ipt = ac.find_template(renWumenu_img, img_array)
    if gongGao_ipt != None:
        pyautogui.moveTo(gonggao_pos)
        time.sleep(0.2)
        pyautogui.leftClick()
        time.sleep(0.9)
        pyautogui.leftClick()
    if ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)), numpy.array(game_over_press_img)) != None:
        pyautogui.keyDown('~')
        pyautogui.keyUp('~')
    #944, 158,1537, 304

def qiandao():
    qiandao_press=ac.find_template(imageGrab(0, 0, 0, 0, "Window_Game", 3),qianda_lingqu_img)
    if  qiandao_press!= None:
        pyautogui.moveTo(929+x1_pos, 869+y1_pos)
        time.sleep(0.1)
        pyautogui.leftClick()
        qiandao_queding_press = ac.find_template(imageGrab(0, 0, 0, 0, "Window_Game", 3),qiandao_queding_img)
        if qiandao_queding_press != None:
            pyautogui.moveTo(799 + x1_pos, 683 + y1_pos)
            time.sleep(0.1)
            pyautogui.leftClick()
            print("签到完成")


def show_game():
   print("发现游戏已启动,请等待..")
   win32gui.ShowWindow(hWnd, 6)  # 将窗口最小化
   win32gui.ShowWindow(hWnd, 1)  # 将窗口最大化并激活    如果只调用这个窗口将无法激活
   time.sleep(0.1)
   rect = windowRect(hWnd)
   ImageGrab.grab(bbox=rect).save("./3rd_imges/3rd_login_img.png")#截取游戏
   pyautogui.keyDown('home')
   pyautogui.keyUp('home')
   pyautogui.keyDown('~')
   pyautogui.keyUp('~')
   time.sleep(0.5)
   pyautogui.keyDown('~')
   pyautogui.keyUp('~')
   pyautogui.keyDown('home')
   pyautogui.keyUp('home')
   while True:
       login_game(hWnd)
       img_array = imageGrab(x1_pos, y2_pos-100, x1_pos+1024, y2_pos, "Window_Game", 4)  # 截全屏numpy
       gaming_panduan = ac.find_template(img_array,gameing_panduan_img)
       if  gaming_panduan != None and login_game(hWnd) is True:
           print()
           print("------------------")
           print("\033[1;32;47m游戏脚本已运行成功\033[0m")
           print("------------------")
           print()
           if ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)),numpy.array(game_over_press_img)) != None:
               pyautogui.keyDown('~')
               pyautogui.keyUp('~')
           break
   print("1秒后脚本开始运行")
   time.sleep(1)
   if game_Home() is True:
       print()
       print("=-主菜单-=")
   qiandao()
   gonggao()
   time.sleep(0.5)
   while True:
       img_array = numpy.array(ImageGrab.grab(bbox=rect))
       zhucaidan = (ac.find_template(img_array,zhucaidan_img))
       if zhucaidan != None:
            break
       else:
           gonggao()
   time.sleep(1)
   renWumenu()

