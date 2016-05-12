# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('champions/') if isfile(join('champions/', f))]
print(onlyfiles)
