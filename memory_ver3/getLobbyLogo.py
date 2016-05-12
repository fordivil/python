# -*- coding: utf-8 -*-
from PIL import Image
import cv2

def getLobbylogo():
    img = Image.open("main.png", mode='r')# 로비기본화면이미지

    a = 15
    b = 20
    c = 155
    d = 70

    iimg = img.crop(
            (
                a,
                b,
                c,
                d
            )
        )


    iimg.save("robby.png") #로비확인용 로고
    image = cv2.imread("robby.png")
    r = 1000.0 / image.shape[1] # 가로세로배율
    dim = (1000, int(image.shape[0] * r)) #가로세로배율
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    # cv2.imshow("scaling",resized)
    # cv2.waitKey(0)
    cv2.imwrite("robby.png",resized)

