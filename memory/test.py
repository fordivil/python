#! C:/Users/vlfgh/Desktop/memory/
# -*- coding: utf-8 -*-


from memorpy import *

mw=MemWorker("LolClient")
l=[x for x in mw.umem_search2("{\"alliedTeam\":[{\"teamId\":")]
#l=[x for x in mw.umem_search("{\"alliedBans\":[")]
#이건아니다
if len(l)>1:
        a = l[0]
        b = a.read(2350).decode('utf-16')
        c = b.split(',')


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

def banlist(b):
    alban = [b[61].split('[')[1],b[62],b[63].split(']')[0]]
    emban = [b[64].split('[')[1],b[65],b[66].split(']')[0]]

    return alban,emban

def emChamList(b):
    emchamlist = [(b[43].split(':')[1].split('}')[0]),(b[47].split(':')[1].split('}')[0]),(b[51].split(':')[1].split('}')[0]),(b[55].split(':')[1].split('}')[0]),(b[59].split(':')[1].split('}')[0])]
    return emchamlist
if len(l)>1:
    print(c)
    print(len(c))
    print(b)
    if len(c)==70 or len(c)==69:
        temp = alliP(c)
        banlist = banlist(c)
        emchamlist = emChamList(c)

        print(temp[2][1])
        print(banlist)
        print(emchamlist)
    if len(c)==66 or len(c)==67 or len(c)==68:
        temp = alliP(c)
        print(temp[0][1])
        #66
        #26
        #28
        #68
        #69


