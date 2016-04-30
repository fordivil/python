#-*- coding: utf-8 -*-
a = '{"alliedTeam":[{"teamId":1,"cellId":0,"summonerName":"소환사137","championPickIntent":0,"championId":0,"assignedPosition":"BOTTOM","spell1Id":4,"spell2Id":7},{"teamId":1,"cellId":1,"summonerName":"Mizco","championPickIntent":0,"championId":0,"assignedPosition":"MIDDLE","spell1Id":12,"spell2Id":4},{"teamId":1,"cellId":2,"summonerName":"Siwang","championPickIntent":0,"championId":0,"assignedPosition":"TOP","spell1Id":14,"spell2Id":4},{"teamId":1,"cellId":3,"summonerName":"160이하여친구함","championPickIntent":0,"championId":0,"assignedPosition":"UTILITY","spell1Id":3,"spell2Id":4},{"teamId":1,"cellId":4,"summonerName":"오호머장군","championPickIntent":0,"championId":0,"assignedPosition":"JUNGLE","spell1Id":11,"spell2Id":4}],"enemyTeam":[{"teamId":2,"cellId":5,"summonerName":"","championId":0},{"teamId":2,"cellId":6,"summonerName":"","championId":0},{"teamId":2,"cellId":7,"summonerName":"","championId":0},{"teamId":2,"cellId":8,"summonerName":"","championId":0},{"teamId":2,"cellId":9,"summonerName":"","championId":0}]},"localPlayerCellId":3,"bans":{"alliedBans":[],"enemyBans":[]},"currentTotalTimeMillis":24000,"currentTimeRemainingMillis":24000,"trades":[]}}   '
a = a.decode('utf-8')
b= a.split(',')
print(type(a))

#플레이어이름
i= 34
c = (b[i].split(':')[1])#2,10,18,26,34 // 적챔프번호 43,47,51,55,59 //우리팀밴 61,적팀밴62
#플레이어 챔프번호
d = (b[i+2].split(':')[1])
#플레이어 포지션
e = (b[i+3].split(':')[1])
#플레이어 1스펠
f = (b[i+4].split(':')[1])
#플레이어 2스펠
g = (b[i+6].split(':')[1])
#print(b[i+5].split(':')[1].split('}')[0]) #울팀 마지막 스펠

#print(b[47].split(':')[1].split('}')[0]) 적챔프번호 따기


#print((b[18].split(':')[1]))


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



temp = alliP(b)
print(temp[4][4])
print(len(b))













