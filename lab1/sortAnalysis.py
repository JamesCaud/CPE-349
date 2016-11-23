#James Caudill

import numpy.random as npRand

def selSort(listA):
   for spot in range(len(listA)):
      posMin = spot
      for loc in range(spot + 1, len(listA)):
         if listA[loc] < listA[posMin]:
            posMin = loc
      
      listA[spot], listA[posMin] = listA[posMin], listA[spot]
   
   return listA    

def mergeSort(listA):
   lists = [[x] for x in listA]
   while len(lists) > 1:
      lists = mergeLists(lists)
   
   return lists[0]

def mergeLists(lists):
   result = []
   for i in range(len(lists) // 2):
      result.append(merge(lists[i * 2], lists[i * 2 + 1]))
   if len(lists) % 2:
      result.append(lists[-1])
   
   return result

def merge(listA, listB):
   i = 0
   j = 0
   result = []
   
   while i < len(listA) and j < len(listB):
      if listA[i] > listB[j]:
         result.append(listB[j])
         j += 1
      else:
         result.append(listA[i])
         i += 1
   
   result.extend(listA[i:])
   result.extend(listB[j:])
  
   return result


def main():
   size = 10000
   timeData = []
   timeData.append(Size, Selection Sort Time, Merge Sort Time)
   
   while (size <= 20000):
      listA = npRand.randint(-10000, 10001, size)
      startSel = time.time()
      selSort(listA)
      endSel = time.time()

      startMerge = time.time()
      mergeSort(listA)
      endMerge = time.time()

      timeData.append(size, endSel-startSel, endMerge-startMerge)
      size += 20


if __name__ == "__main__": main()
