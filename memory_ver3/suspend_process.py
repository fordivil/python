
import psutil


def find_Process_Name(process_name):
    for proc in psutil.process_iter():
        process = psutil.Process(proc.pid)# Get the process info using PID
        pname = process.name()# Here is the process name
        #print pname
        if pname == process_name:
            return proc.pid
somepid = find_Process_Name('LolClient.exe')
print(somepid)
p = psutil.Process(somepid)
while 1:
    data = input('1 = sus, 2= res , 3=exit')
    if data ==1:
        p.suspend()
    elif data ==2:
        p.resume()
    elif data ==3:
        break