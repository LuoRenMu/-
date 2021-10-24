# -*- codeing = utf-8 -*-
# @Time : 2021/10/10 22:23
# @Author : 罗任姆/LoMu
# @File : task.py
# @Software : PyCharm
import numpy
import aircv as ac
import pyautogui
from windowRect import  windowRect
from PIL import ImageGrab
import time
from config import *

def renWumenu():
    print("任务菜单")
    rect = windowRect(hWnd)
    pyautogui.press("home")
    x1_pos, y1_pos, x2_pos, y2_pos = rect
    img_array_renwu = numpy.array(ImageGrab.grab(bbox=rect))
    ipt = ac.find_template(img_array_renwu,renwu_press_img)
    if ipt !=None:
        renWu = (63 + x1_pos, 174 + y1_pos)
        img_array = numpy.array(numpy.array(ImageGrab.grab(bbox=rect)))
        renWu_bool = bool(ac.find_template(img_array,renWumenu_img,0.3))
        time.sleep(0.1)
        pyautogui.moveTo(renWu)
        time.sleep(0.3)
        pyautogui.leftClick()
        time.sleep(0.3)
        if renWu_bool is True:
            pyautogui.moveTo(renWu[0],renWu[1]+80)
            pyautogui.leftClick()
            time.sleep(0.3)
            img_renWuarray = numpy.array(ImageGrab.grab(bbox=rect))
            renWu_Caidan_panduan_bool = bool(ac.find_template(img_renWuarray,renwu_menu_panduan_img,0.7))
            if renWu_Caidan_panduan_bool == False and renWu_bool == True:
                renWulingqu()
        else:
            rect = windowRect(hWnd)
            x1_pos, y1_pos, x2_pos, y2_pos = rect
            gonggao_pos = (1492 + x1_pos, 130 + y1_pos)
            img_array = numpy.array(ImageGrab.grab(bbox=rect))
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
            renWumenu()
    else:
        rect = windowRect(hWnd)
        x1_pos, y1_pos, x2_pos, y2_pos = rect
        gonggao_pos = (1492 + x1_pos, 130 + y1_pos)
        img_array = numpy.array(ImageGrab.grab(bbox=rect))
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
        renWumenu()

def renWulingqu():
    time.sleep(2)
    while True:
        img_array_left =numpy.array(ImageGrab.grab(bbox=(316+x1_pos, 143+y1_pos, 909+x1_pos, 306+y1_pos)))
        # 316, 143, 909, 306
        renWu_lingqu_bool_left = (ac.find_template( img_array_left,renwu_lingqu_img,0.8))
        img_array_right =numpy.array(ImageGrab.grab(bbox=((20+316+x1_pos)*2, 143+y1_pos, (x2_pos-50), 306+y1_pos)))
        renWu_lingqu_bool_right = ac.find_template(img_array_right,renwu_lingqu_img,0.8)
        task_150 = ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)),numpy.array(task_150_img),1)
        task_165 = ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)),numpy.array(task_165_img),1)
        if renWu_lingqu_bool_left != None:
            print()
            print("任务奖励已领取")
            pyautogui.moveTo(812+x1_pos, 263+y1_pos)
            pyautogui.leftClick()
            time.sleep(0.3)
            pyautogui.moveTo(801+x1_pos, 704+y1_pos)
            pyautogui.leftClick()
            time.sleep(1)
        elif renWu_lingqu_bool_right != None:
            print()
            print("任务奖励已领取")
            pyautogui.moveTo(1441+x1_pos,257+y1_pos)
            pyautogui.leftClick()
            time.sleep(0.3)
            pyautogui.moveTo(801+x1_pos, 704+y1_pos)
            pyautogui.leftClick()
            time.sleep(1)
        elif task_150 !=None or task_165 !=None :
            print("使命领取")
            #649, 776  860, 776   1078, 776    1286, 776    1509, 776
            pyautogui.moveTo(649+x1_pos,776+y1_pos)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(795+x1_pos, 708+y1_pos)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(860 + x1_pos, 776 + y1_pos)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(795+x1_pos, 708+y1_pos)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(1078 + x1_pos, 776 + y1_pos)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(795+x1_pos, 708+y1_pos)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(1286 + x1_pos, 776 + y1_pos)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(795+x1_pos, 708+y1_pos)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(1509 + x1_pos, 776 + y1_pos)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(795+x1_pos, 708+y1_pos)
            pyautogui.leftClick()
            print("当前所有任务已完成 -程序结束")
            break
        else:
            renWustart()
            break

def renWustart():
    print()
    print("开始每日任务")
    window_img_array = numpy.array(ImageGrab.grab(bbox=rect))
    yaoristart = ac.find_template(window_img_array, numpy.array(renwu_yaori_start_img), 0.8)
    task_Master_Start = ac.find_template(window_img_array, numpy.array(task_master_img), 0.8)
    game_Coins_Start = ac.find_template(window_img_array,numpy.array(task_game_coins_img),0.8)
    task_team_Start = ac.find_template(window_img_array,numpy.array(task_team_img),0.8)

    if game_Coins_Start != None:
       print("家园福利")
       game_coins_start(game_Coins_Start['result'])

    elif yaoristart != None:
       print("材料活动")
       yaoRi_start(yaoristart['result'])

    elif task_Master_Start != None:
        print("[光与影的彼岸-第十二章]")
        task_master_start(task_Master_Start['result'])
    elif task_team_Start != None:
        print("舰团委托")
        task_team_start(task_team_Start['result'])
    else:
        print("任务结束")

    #elif task  舰团委托
def task_team_start(task_team_Start_pos):
    x, y = task_accept_pos(task_team_Start_pos)
    pyautogui.moveTo(x, y)
    pyautogui.leftClick()
    time.sleep(0.09)
    task_team_submit_pos=ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)),
                     numpy.array(task_team_submit_img), 0.7)
    task_team_submit_ets_pos = ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)),
                                numpy.array(task_team_submit_ets_img), 0.7)
    break1=True
    sum = 0
    while break1:
        if sum == 2:
            break1 = False
        if task_team_submit_pos != None:
            x,y= task_team_submit_pos['result']
            pyautogui.moveTo(xY_pos(x,y))
            time.sleep(0.5)
            pyautogui.leftClick()
            if task_team_submit_ets_pos !=None:
                x, y = task_team_submit_ets_pos['result']
                pyautogui.moveTo(xY_pos(x, y))
                time.sleep(0.5)
                pyautogui.leftClick()
                sum +=1

        else:
            pyautogui.moveTo(xY_pos(219, 833))
            time.sleep(0.5)
            pyautogui.leftClick()
            time.sleep(0.5)
            pyautogui.moveTo(xY_pos(1399, 349))
            time.sleep(0.5)
            pyautogui.leftClick()

def task_master_twelve():
    task_pos = ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)),
                                numpy.array(task_master_twelve_img), 0.7)
    print("[光与影的彼岸-第十二章] 开始")
    pyautogui.moveTo(task_pos['result'] + (x1_pos, y1_pos))
    pyautogui.leftClick()


def task_master_twelve_12_14():
    pyautogui.moveTo(850 + x1_pos, 481 + y1_pos)
    time.sleep(2)
    pyautogui.leftClick()
    sum = 0
    break1 =True
    print("后续将以相对坐标进行处理,请勿操作")
    print("默认进行10次")
    while break1:
        break2 = True
        if sum == task_master_12_14_sum:
            break1 = False
            renWumenu()
        elif ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)), numpy.array(task_master_twelve_12_14_img),0.8) != None:
            pyautogui.moveTo(ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)), numpy.array(task_master_twelve_12_14_img),
                                              0.7)['result']+(x1_pos,y1_pos))
            time.sleep(0.5)
            pyautogui.leftClick()
            time.sleep(0.3)
            pyautogui.press('i')
            time.sleep(0.3)
            pyautogui.press('i')
            time.sleep(0.5)
            while break2:
                if ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)), numpy.array(quchutili_img),0.6) != None:
                    time.sleep(0.5)
                    pyautogui.moveTo(938+x1_pos, 727+y1_pos)
                    time.sleep(1)
                    pyautogui.leftClick()
                    pyautogui.leftClick()
                    time.sleep(0.5)
                    print("取出体力")
                    pyautogui.press('i')
                if ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)), numpy.array(game_loading_img)) == None:
                    break2 = False
                    break3 = True
                    break_t2 = True
                    break_t3 = True
                    time.sleep(3)
                    pyautogui.moveTo(1491 + x1_pos, 71 + y1_pos)
                    pyautogui.leftClick()
                    time.sleep(0.1)
                    pyautogui.leftClick()

                    while break3:
                        if ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)), numpy.array(task_12_14_tiaoguo_img)) != None:
                            pyautogui.moveTo(1021 + x1_pos, 659 + y1_pos)
                            time.sleep(0.5)
                            pyautogui.leftClick()
                            pyautogui.leftClick()
                            time.sleep(0.2)
                            pyautogui.moveTo(1491 + x1_pos, 71 + y1_pos)
                            time.sleep(1.3)
                            pyautogui.leftClick()
                            time.sleep(0.3)
                            print("跳过1")
                            break3 =False

                            while break_t2:
                                if ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)),
                                                    numpy.array(task_12_14_tiaoguo_img)) != None:
                                    break_t2 = False
                                    pyautogui.press('i')
                                    print("跳过2")
                                    pyautogui.moveTo(1491 + x1_pos, 71 + y1_pos)
                                    time.sleep(1.3)
                                    pyautogui.leftClick()
                                    time.sleep(0.5)

                                    while break_t3:
                                        if ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)),
                                                            numpy.array(task_12_14_tiaoguo_img)) != None:
                                            break_t3 = False
                                            pyautogui.press('i')
                                            print("跳过3")
                                            time.sleep(8)
                                            pyautogui.leftClick()
                                            time.sleep(3)
                                            print("已完成[光与影的彼岸-第十二章] 12-14 ")
                                        else:
                                            pyautogui.moveTo(1491 + x1_pos, 71 + y1_pos)
                                            time.sleep(0.5)
                                            pyautogui.leftClick()
                                else:
                                    pyautogui.moveTo(1491 + x1_pos, 71 + y1_pos)
                                    time.sleep(0.5)
                                    pyautogui.leftClick()
                        else:
                            pyautogui.moveTo(1491 + x1_pos, 71 + y1_pos)
                            pyautogui.leftClick()
                            time.sleep(0.5)
                            pyautogui.leftClick()
                if ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)), numpy.array(task_12_14_Act4_img)) != None:
                    pyautogui.moveTo(ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)), numpy.array(task_12_14_over_img))['result']+(x1_pos,y1_pos))
                    pyautogui.keyDown("i")
                    pyautogui.keyUp("i")
                    sum+=1
                    print(f"当前关卡次数{sum}")
        if sum == 0:
            pyautogui.keyDown('right')
            pyautogui.keyUp('right')
            time.sleep(1)
def task_master_start(task_Master_Start):
        x,y = task_accept_pos(task_Master_Start)
        pyautogui.moveTo(x,y)
        pyautogui.leftClick()
        time.sleep(0.09)
        pyautogui.moveTo(850 + x1_pos, 481 + y1_pos)
        break1 = True
        while break1:
            if ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)),numpy.array(task_master_one_img),0.7) == None:
                if ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)), numpy.array(task_master_twelve_img),0.7) != None:
                    task_master_twelve()
                    task_master_twelve_12_14()
                    break1 = False
                else:
                    print("正在向左寻找 [光与影的彼岸-第十二章] ")
                    pyautogui.scroll(-10)
            else:
                while break1:
                    if ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)), numpy.array(task_master_twelve_img),0.7) != None:
                        task_master_twelve()
                        task_master_twelve_12_14()
                        break1 = False
                    else:
                        print("正在向右寻找 [光与影的彼岸-第十二章]")
                        pyautogui.scroll(10)
        task_progress['task_master'] = 1

def game_coins_start(game_conins_pos):
        x,y=task_accept_pos(game_conins_pos)
        pyautogui.moveTo(x,y)
        pyautogui.leftClick()
        time.sleep(0.09)
        if ac.find_template(numpy.array(ImageGrab.grab(bbox=rect)),numpy.array(task_home_walfare_img),0.3) != None:
            time.sleep(1)
            pyautogui.moveTo(450+x1_pos, 201+y1_pos) #体力 x - 200
            time.sleep(0.5)
            print("调用易键鼠点击")
            objdll.M_LeftClick(hdl, 1)
            time.sleep(1)
            pyautogui.moveTo(250 + x1_pos, 201 + y1_pos)
            time.sleep(0.5)
            objdll.M_LeftClick(hdl, 1)
            time.sleep(0.5)
            pyautogui.moveTo(938 + x1_pos, 727 + y1_pos)
            objdll.M_LeftClick(hdl, 1)
            task_progress['game_coins'] = 1
            pyautogui.keyDown('`')
            pyautogui.keyUp('`')
            renWumenu()
        else:
            pyautogui.keyDown('`')
            pyautogui.keyUp('`')
            renWumenu()

def yaoRi_start(pos):
    x, y = task_accept_pos(pos)
    pyautogui.moveTo(x, y)
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