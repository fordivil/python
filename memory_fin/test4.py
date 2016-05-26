#! C:/Users/vlfgh/Desktop/memory/
# -*- coding: utf-8 -*-

import isThereLol
import random
from memorpy import *
def le():
    return 1

def chk():

    if isThereLol.isThereLol():
        mw=MemWorker("LolClient")
        l=[x for x in mw.umem_search("{\"alliedTeam\":[{\"teamId\":")]
        while True:
            print('메모리서치 중  ' + str(len(l)))
            if len(l)==0:
                l = [x for x in mw.umem_search4("{\"alliedTeam\":[{\"teamId\":")]
            if(len(l)>0):
                break

        def le():
            print("검색중")
            l = [x for x in mw.umem_search4("{\"alliedTeam\":[{\"teamId\":")]
            while True:
                print('메모리서치 중  ' + str(len(l)))
                if len(l) == 0:
                    l = [x for x in mw.umem_search4("{\"alliedTeam\":[{\"teamId\":")]
                if (len(l) > 0):
                    break
            return l




        def banlist(b):
            alban = (b.split('[')[3].split(']')[0]).split(',')
            emban = b.split('[')[4].split(']')[0].split(',')

            return alban, emban

        def emChamList(b):
            emchamlist = [(b[43].split(':')[1].split('}')[0]), (b[47].split(':')[1].split('}')[0]),
                          (b[51].split(':')[1].split('}')[0]), (b[55].split(':')[1].split('}')[0]),
                          (b[59].split(':')[1].split('}')[0])]
            return emchamlist


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


    z= 0
    str1 = {}
    a = 0
    set1 = 0
    set2 = 0
    set3 = 0
    set4 = 0
    set5 = 0
    set6 = 0
    set7 = 0
    set8 = 0
    set9 = 0
    set10 = 0
    set11 = 0
    set12 = 0
    set13 = 0
    set14 = 0
    set15 = 0
    set16 = 0






    while True:
        print('while문 접근')
        if z!=0:
            break

        l = le()


        for i in l:

            if str(i).split(':')[1] in str1.values():
                continue

            try:



                b = i.read(2350).decode('utf-16')

            except:
                b= ''
                pass
            c = b.split(',')
            if len(l)>1 and len(b)!=0:

                if len(c)>60: #정보를 알아낼수있는 주소라면
                    str1[a] = str(i).split(':')[1]
                    if len(c)<65:
                        continue
                    a += 1



                    temp = alliP(c)
                    echm  = emChamList(c)
                    ban = banlist(b)

                    #한번보냇으면 서버로 더 보내면 안됨
                    if len(ban[0])==1 and ban[0][0]!='' and set1!=1:#울팀 1밴
                        set1 = 1
                        print("울팀 1밴")
                        print(ban[0][0])

                    if len(ban[0]) == 2 and set2!=1:  # 울팀 2밴
                        set2 = 1
                        print("울팀 2밴")
                        print(ban[0][1])

                    if len(ban[0]) == 3 and set3!=1:  # 울팀 3밴
                        set3 = 1
                        print("울팀 3밴")
                        print(ban[0][2])

                    if len(ban[1]) == 1 and ban[1][0]!="" and set4!=1:  # 적팀 1밴
                        set4 = 1
                        print("적팀 1밴")
                        print(ban[1][0])


                    if len(ban[1]) == 2  and set5!=1 :  # 적팀 2밴
                        set5 = 1
                        print("적팀 2밴")
                        print(ban[1][1])

                    if len(ban[1]) == 3 and  set6!=1:  # 적팀 3밴
                        set6 = 1
                        print("적팀 3밴")
                        print(ban[1][2])


                    if temp[0][1] !='0'  and set7!=1 and temp[0][1]!=0: #울팀 1픽 챔프
                        set7 = 1


                        print('울팀 1픽 챔프')

                        print(temp[0][1])
                    if temp[1][1] != '0' and set8!=1 and temp[1][1]!=0:  # 울팀 2픽 챔프
                        set8 = 1

                        print('울팀 2픽 챔프')
                        print(temp[1][1])
                    if temp[2][1] != '0' and set9!=1 and temp[2][1]!=0:  # 울팀 3픽 챔프
                        set9 = 1

                        print('울팀 3픽 챔프')
                        print(temp[2][1])
                    if temp[3][1] != '0' and set10!=1 and temp[3][1]!=0 and temp[3][1]!=''"CHAMPION_SELECT"'' and temp[4][1]!='"BAN':  # 울팀 4픽 챔프
                        set10 = 1

                        print('울팀 4픽 챔프')
                        print(temp[3][1])
                    if temp[4][1] != '0' and set11!=1 and temp[4][1]!=0 and temp[4][1]!='"BAN':  # 울팀 5픽 챔프
                        set11 = 1

                        print('울팀 5픽 챔프')
                        print(temp[4][1])
                    if echm[0]!='0' and set12!=1 and echm[0]!=0:  #적팀 1픽 챔프
                        set12 = 1

                        print('적팀 1픽 챔프')
                        print(echm[0])
                    if echm[1] != '0' and set13!=1 and echm[1]!=0:  # 적팀 2픽 챔프
                        set13 = 1

                        print('적팀 2픽 챔프')
                        print(echm[1])
                    if echm[2] != '0' and set14!=1 and echm[2]!=0:  # 적팀 3픽 챔프
                        set14 = 1

                        print('적팀 3픽 챔프')
                        print(echm[2])
                    if echm[3] != '0' and set15!=1 and echm[3]!=0:  # 적팀 4픽 챔프
                        set15 = 1

                        print('적팀 4픽 챔프')
                        print(echm[3])
                    if echm[4] != '0' and set16!=1 and echm[4]!=0:  # 적팀 5픽 챔프
                        set16 = 1

                        print('적팀 5픽 챔프')
                        print(echm[4])








                    if temp[4][1]!='0' and echm[4]!='0': #아군,적 픽이 모두 끝난상황
                        print('다끝남')
                        z=1
                        break














    else:
        print('banpicstatement - 클라못찾음')

chk()




