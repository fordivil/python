from memorpy import *

mw=MemWorker("LolClient")
l=[x for x in mw.umem_search("{\"alliedTeam\":[{\"teamId\":")]
a = l[0]
b = a.read(1500).decode("utf-16-le")

print(b)