#-*- coding: utf-8 -*-
import isThereLol
from memorpy import *
#a = '{"alliedTeam":[{"teamId":1,"cellId":0,"summonerName":"소환사137","championPickIntent":0,"championId":0,"assignedPosition":"BOTTOM","spell1Id":4,"spell2Id":7},{"teamId":1,"cellId":1,"summonerName":"Mizco","championPickIntent":0,"championId":0,"assignedPosition":"MIDDLE","spell1Id":12,"spell2Id":4},{"teamId":1,"cellId":2,"summonerName":"Siwang","championPickIntent":0,"championId":0,"assignedPosition":"TOP","spell1Id":14,"spell2Id":4},{"teamId":1,"cellId":3,"summonerName":"160이하여친구함","championPickIntent":0,"championId":0,"assignedPosition":"UTILITY","spell1Id":3,"spell2Id":4},{"teamId":1,"cellId":4,"summonerName":"오호머장군","championPickIntent":0,"championId":0,"assignedPosition":"JUNGLE","spell1Id":11,"spell2Id":4}],"enemyTeam":[{"teamId":2,"cellId":5,"summonerName":"","championId":0},{"teamId":2,"cellId":6,"summonerName":"","championId":0},{"teamId":2,"cellId":7,"summonerName":"","championId":0},{"teamId":2,"cellId":8,"summonerName":"","championId":0},{"teamId":2,"cellId":9,"summonerName":"","championId":0}]},"localPlayerCellId":3,"bans":{"alliedBans":[203,11],"enemyBans":[76,245]},"currentTotalTimeMillis":30000,"currentTimeRemainingMillis":30000,"trades":[]}} '
mw = MemWorker("LolClient")
l = [x for x in mw.umem_search("{\"alliedTeam\":[{\"teamId\":")]
print(l)
a = l[0]
a =a.read(2350).decode('utf-16')
b= a.split(',')





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
    alban = a.split('[')[3].split(']')[0]
    emban = a.split('[')[4].split(']')[0]



    return alban,emban

def emChamList(b):
    emchamlist = [(b[43].split(':')[1].split('}')[0]),(b[47].split(':')[1].split('}')[0]),(b[51].split(':')[1].split('}')[0]),(b[55].split(':')[1].split('}')[0]),(b[59].split(':')[1].split('}')[0])]
    return emchamlist



temp = alliP(b)

print(emChamList(b))
print(banlist(b))
print(temp[0][0])
print(temp[1][0])
print(temp[2][0])
print(temp[3][0])
print(temp[4][0])
print(temp[0][1])
print(temp[1][1])
print(temp[2][1])
print(temp[3][1])
print(temp[4][1])
print(len(b))














