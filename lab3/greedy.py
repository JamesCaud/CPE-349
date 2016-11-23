"""
Mini-triathlon with only one kid in the pool at a time.
James Caudill
CPE 349
11/01/16
"""

import sys
import ast

camperDict = {}
camperList = []
runningTime = 0
totalTime = 0

def cusSort(s):
    return sum(s[1:]) 

with open(sys.argv[1], 'r') as inFile:
    s = inFile.read().replace('\n', ', ')
    s = "{" + s + "}"
    camperDict = ast.literal_eval(s)

camperList = camperDict.values()

camperList.sort(key=cusSort, reverse=True)

while camperList:
    for k, v in camperDict.items():
        if v == camperList[0]:
            if totalTime < runningTime + sum(v):
                totalTime = runningTime + sum(v)
            runningTime = runningTime + v[0]
            print (k)
            del camperDict[k]
            camperList.pop(0)
print (totalTime)
