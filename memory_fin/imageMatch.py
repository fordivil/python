# -*- coding: utf-8 -*-
import cv2



def imageMatch(image1,image2):
    img_rgb = cv2.imread(image1)
    img2 = cv2.imread(image2)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, img_gray2, cv2.TM_CCOEFF_NORMED)
    mn, _, mnLoc, _ = cv2.minMaxLoc(res)
    #print mn,_,mnLoc

    return mn,_,mnLoc


