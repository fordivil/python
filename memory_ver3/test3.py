from PIL import Image
from os import listdir
from os.path import isfile, join
import imageMatch
onlyfiles = [f for f in listdir('champions/') if isfile(join('champions/', f))]

for i in onlyfiles:
    im = Image.open('champions/'+i)
    im = im.resize((35, 35), Image.ANTIALIAS)
    im.save('recham/'+i, 'png', quality=100)



