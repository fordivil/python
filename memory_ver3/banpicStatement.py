#! C:/Users/vlfgh/Desktop/memory/
# -*- coding: utf-8 -*-

import isThereLol
from memorpy import *

def chk():

    if isThereLol.isThereLol():
        mw=MemWorker("LolClient")
        l=[x for x in mw.umem_search("{\"alliedTeam\":[{\"teamId\":")]
        while True:
            if len(l)==0:
                l = [x for x in mw.umem_search("{\"alliedTeam\":[{\"teamId\":")]
                if(len(l)>1):
                    break

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



    while True:

        for i in l:
            time.sleep(1)


            b = i.read(2350).decode('utf-16')
            c = b.split(',')
            if len(l)>1:

                if len(c)>60: #정보를 알아낼수있는 주소라면

                    temp = alliP(c)
                    echm  = emChamList(c)
                    ban = banlist(c)

                    #한번보냇으면 서버로 더 보내면 안됨
                    if len(ban[0])==1:#울팀 1밴
                        print("울팀 1밴")
                    if len(ban[0]) == 2:  # 울팀 2밴
                        print("울팀 2밴")
                    if len(ban[0]) == 3:  # 울팀 3밴
                        print("울팀 3밴")
                    if len(ban[1]) == 1:  # 적팀 1밴
                        print("적팀 1밴")
                    if len(ban[1]) == 2:  # 적팀 2밴
                        print("적팀 2밴")
                    if len(ban[1]) == 3:  # 적팀 3밴
                        print("적팀 3밴")
                    if temp[0][1] != 0 : #울팀 1픽 챔프
                        print('울팀 1픽 챔프')
                    if temp[1][1] != 0:  # 울팀 2픽 챔프
                        print('울팀 2픽 챔프')
                    if temp[2][1] != 0:  # 울팀 3픽 챔프
                        print('울팀 3픽 챔프')
                    if temp[3][1] != 0:  # 울팀 4픽 챔프
                        print('울팀 4픽 챔프')
                    if temp[4][1] != 0:  # 울팀 5픽 챔프
                        print('울팀 5픽 챔프')
                    if echm[0]!=0:  #적팀 1픽 챔프
                        print('적팀 1픽 챔프')
                    if echm[1] != 0:  # 적팀 2픽 챔프
                        print('적팀 2픽 챔프')
                    if echm[2] != 0:  # 적팀 3픽 챔프
                        print('적팀 3픽 챔프')
                    if echm[3] != 0:  # 적팀 4픽 챔프
                        print('적팀 4픽 챔프')
                    if echm[4] != 0:  # 적팀 5픽 챔프
                        print('적팀 5픽 챔프')




                    if temp[4][1]!=0 and echm[4]!=0: #아군,적 픽이 모두 끝난상황
                        print('다끝남')
                        break








    else:
        print('banpicstatement - 클라못찾음')




