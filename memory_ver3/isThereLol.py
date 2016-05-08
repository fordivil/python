import finPID_by_processName


def isThereLol():
    if finPID_by_processName.find_Process_Name('LolClient.exe') == 0:
        print('isthereli is false')
        return False
    else:
        print('istherlol is ture')
        return True