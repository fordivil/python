# -*- coding: utf-8 -*-
import time
import isThereLol
import mainOrbanpick




while 1:
    if isThereLol.isThereLol() == True:
        lobbystate = mainOrbanpick.mainoRbanpick()
        if lobbystate == False:#lol 클라 못찾을경우
            break
    print('Wating lolClient')
    time.sleep(3)





