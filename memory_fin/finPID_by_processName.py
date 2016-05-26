import psutil


def find_Process_Name(process_name):
    for proc in psutil.process_iter():


        process = psutil.Process(proc.pid)# Get the process info using PID
        pname = process.name()# Here is the process name


        #print pname
        if pname == process_name:
            return proc.pid
    return 0




print(find_Process_Name("LolClient.exe"))