from PIL import Image

def capture_userName():
    img = Image.open("1234.png", mode='r')

    x= 0
    a = 110
    b = 120
    c = 250
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
        iimg.save("Mname"+str(x)+".png")
        x+=1




