# 你有很多事情可以做 但不是来观看这份大便
嗯 这是一份初学者的答卷 可以说是烂到狗屎











#### 崩坏三从启动到完成每日任务 及经验刷取
这是一个半成品脚本 或许此脚本可以完成所有任务 或许会因为未知bug而中断 

但是它能有效执行12-14关卡经验刷取 你可以在 config文件中的注释看到它的默认关卡执行次数 你也可以对此进行修改

使用它 你需要安装 python-opencv aircv numpy pyautogui Piliow win32api pywin32 

并且使用1600-900窗口分辨率 启动游戏需在config中更改位置 推荐使用绝对路劲

整体上的代码没有任何技术含量 由于制作技术低廉 前期整体框架搭建过于杂乱  便停止对其维护

它的原理非常简单 只是获取图像 对图像进行识别判断  但它会判断登陆时发生的各种错误! 并有效的解决它

如果你使用的是官方渠道账号 没有发生未知bug的情况下 那么它会从启动到结束完全自动的运行至结束

而在任务方面 还有最后一项 舰团奖励领取 这一块 我没有进行测试 具体bug错误 是未知的

此项目为早期学习 直接调用opencv的图像模板匹配库 此项目仅为留恋 毫无技术含量可言

test为运行

===============================
整体框架中 有大量未调用函数 及 未编写完成函数 
