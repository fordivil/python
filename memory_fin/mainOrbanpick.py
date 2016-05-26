# -*- coding: utf-8 -*-
import getScreenShot_by_winTitle
import getLobbyLogo
import imageMatch
import time
import banpicStatement


def mainoRbanpick():

    if getScreenShot_by_winTitle.screenshot('main')==False:#화면찍는데 lol클라 못찾을경우
        print('mainOrbanpick is false')
        return False
    getLobbyLogo.getLobbylogo() #로비 로고 찍기 lobby.png 로저장됨
    currentstatement = imageMatch.imageMatch('Ori_robby.png', 'robby.png')# 기존로비랑 현재찎은로비로고 비교
    if currentstatement[0]>0.8:#로비라면
        print(currentstatement)
        print("still Lobby")
        return 1
    else:#밴화면인지확인
        statement = imageMatch.imageMatch('isban.png', 'robby.png')
        if statement[0] > 0.8:
            print('밴픽화면')
            banpicStatement.chk()
        else:
            print("밴로비 둘다아님")









