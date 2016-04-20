from PIL import Image
import cv2

def capture_userName():
    img = Image.open("1234.png", mode='r')

    x= 0
    a = 114
    b = 120
    c = 235
    d = 145

    z=80

    while x<5:
        if(x>0):
            b+=z
            d+=z

        iimg = img.crop(
            (
                a,
                b,
                c,
                d
            )
        )


        iimg.save("Mname33"+str(x)+".png")
        image = cv2.imread("Mname33"+str(x)+".png")
        r = 1000.0 / image.shape[1] # 가로세로배율
        dim = (1000, int(image.shape[0] * r)) #가로세로배율
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
       # cv2.imshow("scaling",resized)
       # cv2.waitKey(0)
        cv2.imwrite("Mname33"+str(x)+".png",resized)
        x+=1




