#! C:/Users/vlfgh/Desktop/memory/
# -*- coding: utf-8 -*-

import isThereLol
from memorpy import *

def chk():

    if isThereLol.isThereLol():
        mw=MemWorker("LolClient")
        l=[x for x in mw.umem_search2("{\"alliedTeam\":[{\"teamId\":")]
        if len(l)>1:
                a = l[0]
                b = a.read(2350).decode('utf-16')
                c = b.split(',')
        else:
            time.sleep(3)
            l = [x for x in mw.umem_search2("{\"alliedTeam\":[{\"teamId\":")]


        def alliP(b):
            list = [2,10,18,26,34]
            list2 = [0,2,3,4,6]
            a = 0
            aa=0
            player = [0,0,0,0,0]
            result = [0,0,0,0,0]


            for i in list:
                for z in list2:
                    if(i==34 and z==6):
                        player[a] = (b[i+5].split(':')[1].split('}')[0])
                        break

                    player[a]= (b[i+z].split(':')[1])
                    a = a+1
                result[aa] = player
                player = [0,0,0,0,0]
                a = 0
                aa = aa+1
            return result



        if len(l)>1:
            if len(c)==66 or len(c)==67 or len(c)==68 or len(c)==70 or len(c)==69:
                temp = alliP(c)
                x= 0
                y = 5
                while x<5:

                    for z in temp:
                        print(temp[x][len(temp)-y])
                        y+=1
                    x+=1

                #66
                #26
                #28
                #68
                #69
    else:
        print('banpicstatement - 클라못찾음')


