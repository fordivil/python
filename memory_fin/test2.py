#-*- coding: utf-8 -*-
import isThereLol
from memorpy import *
a = '"alliedTeam":[{"teamId":2,"cellId":5,"summonerName":"불화염파이어","championPickIntent":0,"championId":111,"assignedPosition":"JUNGLE","spell1Id":11,"spell2Id":4},{"teamId":2,"cellId":6,"summonerName":"160이하여친구함","championPickIntent":0,"championId":19,"assignedPosition":"UTILITY","spell1Id":14,"spell2Id":4},{"teamId":2,"cellId":7,"summonerName":"복수의시작","championPickIntent":0,"championId":41,"assignedPosition":"TOP","spell1Id":12,"spell2Id":4},{"teamId":2,"cellId":8,"summonerName":"올해군대가니즐겜","championPickIntent":0,"championId":81,"assignedPosition":"BOTTOM","spell1Id":7,"spell2Id":4},{"teamId":2,"cellId":9,"summonerName":"조녹환","championPickIntent":0,"championId":0,"assignedPosition":"MIDDLE","spell1Id":3,"spell2Id":4}],"enemyTeam":[{"teamId":1,"cellId":0,"summonerName":"","championId":106},{"teamId":1,"cellId":1,"summonerName":"","championId":15},{"teamId":1,"cellId":2,"summonerName":"","championId":161},{"teamId":1,"cellId":3,"summonerName":"","championId":0},{"teamId":1,"cellId":4,"summonerName":"","championId":0}]},"localPlayerCellId":6,"bans":{"alliedBans":[76,13,203],"enemyBans":[12,245,238]},"currentTotalTimeMillis":30000,"currentTimeRemainingMillis":18036,'

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















