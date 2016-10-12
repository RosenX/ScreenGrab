#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
  
  
import pythoncom  
import pyHook  
import time
import os

image_path = 'ImageGrabed'

def onKeyboardEvent(event):   
    # 监听键盘事件
    if event.Key == 'F6':
        from PIL import ImageGrab
        image_name = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time())) + '.png'
        print 'Grap %s' % image_name
        image = ImageGrab.grab()
        image.save(image_path + '/' + image_name)
    return True
  
  
  
  
if __name__ == "__main__":

    if not os.path.exists(image_path): os.mkdir(image_path)
    
    #创建hook句柄  
    hm = pyHook.HookManager()
  
    #监控键盘
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()

    #循环获取消息  
    pythoncom.PumpMessages()  