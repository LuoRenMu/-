# -*- codeing = utf-8 -*-
# @Time : 2021/10/10 12:17
# @Author : 罗任姆/LoMu
# @File : config.py
# @Software : PyCharm
import aircv as ac
import win32api
import win32gui
from open3rd_win32 import *
import time
from windowRect import windowRect
import ctypes

objdll= ctypes.windll.LoadLibrary('./msdk.dll') #此处是易键鼠程序载入 可将金币领取更改为系统api调用 因为会发生点击无效错误所以使用了易键鼠
hdl = objdll.M_Open(1)
login_press_img_source = ac.imread("3rd_imges/3rd_login_press_source.png")
login_xieyi_img_source = ac.imread("3rd_imges/3rd_login_xieyi_source.png")
login_xieyi_press_source = ac.imread("3rd_imges/3rd_login_xieyi_press_source.png")
login_press_click_source = ac.imread("3rd_imges/3rd_login_press_click_source.png")
login_exit_img = ac.imread("3rd_imges/3rd_login_wangluo.png")
zhucaidan_img = ac.imread("3rd_imges/zhucaidan.png")
renWumenu_img = ac.imread("3rd_imges/renWucaidan_img.png")
gonggao_img = ac.imread("3rd_imges/gonggao.png")
renwu_lingqu_img = ac.imread("3rd_imges/renwu_lingqu.png")
renwu_menu_panduan_img = ac.imread("3rd_imges/renWuCaidanpanduan.png")
gameing_panduan_img  = ac.imread("3rd_imges/3rd_gameing_panduan.png")
qianda_lingqu_img = ac.imread("3rd_imges/qiandaolingqu.png")
qiandao_queding_img = ac.imread("3rd_imges/qiandao_queding.png")
renwu_press_img = ac.imread("3rd_imges/renwu_press.png")
renwu_yaori_start_img = ac.imread("3rd_imges/yaori_start_img.png")
game_home_img = ac.imread("3rd_imges/3rd_home_img.png")
task_master_img = ac.imread("3rd_imges/renWu_juqingguanka.png")
task_game_coins_img = ac.imread("3rd_imges/game_coins.png")
task_home_walfare_img = ac.imread("3rd_imges/home_Welfare_img.png")
task_master_one_img = ac.imread("3rd_imges/task_one_img.png")
task_master_twelve_img = ac.imread("3rd_imges/task_master_twelve.png")
game_over_press_img = ac.imread("3rd_imges/game_over_press.png")
task_master_twelve_12_14_img = ac.imread("3rd_imges/take_master_twelve_12_14.png")
game_loading_img = ac.imread("3rd_imges/game_loading.png")
task_150_img = ac.imread("3rd_imges/task_150.png")
task_165_img = ac.imread("3rd_imges/165.png")
task_12_14_over_img = ac.imread("3rd_imges/task_12_14_over.png")
quchutili_img = ac.imread("3rd_imges/tili.png")
task_12_14_tiaoguo_img = ac.imread("3rd_imges/tiaoguo.png")
task_12_14_Act4_img = ac.imread("3rd_imges/tast_12_14_overAct4.png")
task_team_img = ac.imread("3rd_imges/task_team.png")
task_team_submit_img =ac.imread("3rd_imges/task_team_submit.png")
task_team_submit_ets_img = ac.imread("3rd_imges/task_team_submit_ets.png")
i = 0
#检测游戏是否已启动 如果未启动则 启动
if bool(win32gui.FindWindow("UnityWndClass", None)) is False:
    i = -3
    print("未发现游戏,正在启动游戏")
    try:
        win32api.ShellExecute(0, 'open', r'D:\3rd\BH3.exe', '', '', 1)  # 打开文件 绝对路劲
    except Exception:
        print("D:\3rd\BH3.exe目标不存在")
        print("请将快捷启动放置当前目录,或手动启动")
    while True:
        i += 3
        hWnd = win32gui.FindWindow("UnityWndClass", None)
        print(f"游戏启动已耗时{i}秒")
        time.sleep(3)
        if i == 30: print("网络可能发生错误,导致启动延长")
        if bool(hWnd) is True:
            print(f"游戏启动成功 总耗时{i + 3}秒")
            break
else: #返回坐标
    hWnd = win32gui.FindWindow("UnityWndClass", None)

def whilerect():
    hWnd = win32gui.FindWindow("UnityWndClass", None)
    rect = windowRect(hWnd)
    return rect


rect = win32gui.GetWindowRect(hWnd)
x1_pos,y1_pos,x2_pos,y2_pos = rect
w = rect[2] - x1_pos
h = rect[3] - y1_pos
if w>1700 and h > 1000:
    print("请使用1600-900窗口分辨率")
    exit()
def task_accept_pos(task_pos):
    x,y = task_pos
    task_start_x1_pos = x1_pos+188+x
    task_start_y1_pos = y1_pos+34+y
    return task_start_x1_pos,task_start_y1_pos

task_master_12_14_sum = 10 #设置12-14关卡执行次数

def xY_pos(xY_pos,yX_pos):
   return xY_pos+x1_pos,yX_pos+y1_pos
task_sum = [0]

task_progress = {"yaori":None,"task_master":None,"game_coins":None}
