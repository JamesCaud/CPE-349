#James Caudill

import sys

def findNumLin(lst):
   for i in range(0, len(lst), 2):
      if int(lst[i]) != int(lst[i+1]):
         return lst[i]
   return lst[-1]

def findNumBS(lst, low, high):
   if low > high:
      return "None"
   if low == high:
      return lst[low]
   mid = (low + high)//2
   if mid%2:
      if lst[mid] == lst[mid-1]:
         return findNumBS(lst, mid+1, high)
      else:
         return findNumBS(lst, low, mid-1)
   else:
      if lst[mid] == lst[mid+1]:
         return findNumBS(lst, mid+2, high)
      else:
         return findNumBS(lst, low, mid)

with open(sys.argv[1], 'r') as inFile:
   inList = inFile.readline()
   inList = inList[1:-2]
   inList = inList.split(',')

print (findNumBS(inList, 0, len(inList)-1))
