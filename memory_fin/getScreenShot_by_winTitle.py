#! C:/Users/vlfgh/Desktop/memory/
# -*- coding: utf-8 -*-


import win32gui
import win32ui
import win32con
import pid_to_hwnd
import finPID_by_processName
import isThereLol
import time

import getUser_resolution
def screenshot(name):


    user_H_W =  getUser_resolution.getUserResolution()
    h = 1280
    w = 800

    d = ((user_H_W[0]-h)//2)
    dd = ((user_H_W[1]-w)//2)






    if isThereLol:
        hwnd = pid_to_hwnd.get_hwnds_for_pid(finPID_by_processName.find_Process_Name("LolClient.exe"))

        if len(hwnd)==0:
            time.sleep(10)
        hwnd = hwnd[0]
        win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST,d,dd,1280,800,0)
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, h,w)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(h, w) , dcObj, (0,0), win32con.SRCCOPY)
        dataBitMap.SaveBitmapFile(cDC, name+".png")
        # Free Resources
        dcObj.DeleteDC()
        #cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
    else:
        print('getScreenChot_by_wintitle is false')
        return False



