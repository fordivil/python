import cv2



def IMG_matching(img,tempIMGlist):
    img_rgb = img
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    result = [0,0,0,0,0]
    result1 = ["top","mid","jg","ad","sup"]
    x=0
    for template in tempIMGlist:
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        cv2.normalize(res, res, 0, 1, 32)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_loc[1]<150:  #1픽 포지션

            result[0]=result1[x]
        elif max_loc[1]>150 and max_loc[1]<250: #2픽 포지션

            result[1] = result1[x]
        elif max_loc[1]>250 and max_loc[1]<350: #3픽 포지션

            result[2] = result1[x]
        elif max_loc[1] > 350 and max_loc[1] < 400: #4픽 포지션

            result[3] = result1[x]
        elif max_loc[1] > 400 and max_loc[1] < 500: #5픽 포지션

            result[4] = result1[x]
        x+=1
    return result



