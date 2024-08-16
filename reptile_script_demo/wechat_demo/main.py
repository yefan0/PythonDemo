from wxauto import *
import time
import random

listtime = []

while True:
    time_now = time.strftime("%H:%M:%S", time.localtime())
    if time_now == "07:58:00":
        for i in range(1):
    
            # 函数返回参数1和参数2之间的任意整数， 闭区间
            a=random.randint(10,55)
            # str(a).zfill(2)代表不足两位的字符向左补0
            listtime = '08:'+ str(a).zfill(2) + ':10'
            print(listtime)
            time.sleep(2)

    

    time_do = time.strftime("%H:%M:%S", time.localtime())
    
    if time_do == listtime:
        # 获取当前微信客户端
        wx = WeChat()
        # 获取会话列表
        who = 'yefan'
        wx.ChatWith(who=who)
        # 向某人发送消息（以`文件传输助手`为例）
        msg = '早' 
        wx.SendMsg(msg, who) # 向`文件传输助手`发送消息：你好~
        # 切换到通讯录页面
        wx.SwitchToChat()
        time.sleep(2)

    time_end = time.strftime("%H:%M:%S", time.localtime())
    if time_now == "09:00:00":
        listtime = []

