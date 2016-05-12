from PIL import Image



im = Image.open("Mname33" + str(x) + ".png")
        im = im.resize((632,125),Image.ANTIALIAS)
        im.save("resiz"+ str(x) +".png",'png',quality=100)
