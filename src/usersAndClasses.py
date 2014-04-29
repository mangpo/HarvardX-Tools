#!/usr/bin/env python

import os
import glob
import user
import csv
import ipGeoloc as loc
import sys

class userClasses:
    def __init__(self, uname, className):
        self.numClasses = 1
        self.uname = uname
        self.country = ''
        self.classList = [className]
    

geoFile = csv.reader(open(sys.argv[1], 'r'))
geoDict = loc.builddict(geoFile)

dirList = glob.glob('[A-Z]*')
classDict = {}

for d in dirList:
    filein = open(d+'/users.csv', 'r')
    fin = csv.reader(filein)
    cName = d
    fin.next()
    udict = user.builddict(fin)
    for u in iter(udict):
        if u in classDict:
            classDict[u].numClasses += 1
            classDict[u].classList.append(cName)
            if udict[u].username != classDict[u].uname:
                classDict[u].uname = 'Duplicate user name'
        else:
            classDict[u] = userClasses(udict[u].username, cName)
            if udict[u].username in geoDict:
                classDict[u].country = geoDict[udict[u].username]

    filein.close()

outf = csv.writer(open('studentClassList.csv', 'w'))
outf.writerow(['user Id', 'User name','country', 'number of classes', 'classes'])
for u in iter(classDict):
    outf.writerow([u, classDict[u].uname, classDict[u].country, classDict[u].numClasses, classDict[u].classList])
