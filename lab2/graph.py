from compiler.ast import flatten
import sys

"""
createList creates and initializes a dict acting as a edge list
it returns the dictionary
does not allow adding the same node as a neighbor to itself
reads in edges from command line
"""
def createList():
   retDict = {}
   with open(sys.argv[1], 'r') as inFile:
      for line in inFile:
         tup = line.strip()
         tup = tup.split(' ')
         tup[0], tup[1] = int(tup[0]), int(tup[1])
         if tup[0] != tup[1]:
            if tup[0] in retDict.keys():
               retDict[tup[0]].append(tup[1])
            else:
               retDict[tup[0]] = [tup[1]]
            if tup[1] in retDict.keys():
               retDict[tup[1]].append(tup[0])
            else:
               retDict[tup[1]] = [tup[0]]
   return retDict

"""
addColorAttr inserts a color attribute to all lists for each node
takes a graph and inserts based on reference
"""
def addColorAttr(graph):
   for k, v in graph.items():
      v.insert(0, 'N/C')

"""
switchColor switches color from black to white and vice versa
takes in a string of color and returns new color
"""
def switchColor(color):
   if color == 'W':
      return 'B'
   else:
      return 'W'

"""
colorGraph does the BFS and colors each node, it also counts the connected components
It takes a graph dict
returns the number of connected components and if the WHOLE graph is two colorable
if any connected component is not two colorable it will return false as suggested in spec
"""
def colorGraph(graph):
   conComp = 0
   color = 'B'
   twoColor = True
   queue = []
   addColorAttr(graph)

   # loop through all nodes in graph edge dictionary
   for k, v in graph.items():
      # only start the BFS if the node has no color
      if v[0] == 'N/C':
         conComp = conComp + 1
         v[0] = color
         color = switchColor(color)      
         queue = v[1:]
         # loop as long as their are neighbors in the graph uncolored
         while queue:
            # print ("in queue, color = %s" % (color))
            popList = queue
            queue = []
            # print(popList)
            # loop through next layer of nodes
            for node in popList:
               # if uncolored, color then add neighbors to next layer list
               if graph[node][0] == 'N/C':
                  graph[node][0] = color
                  queue.insert(0,graph[node][1:])
                  # print ('node %d %s' % (node, color))
               # if the nodes color is wrong, we know it's not two colorable
               elif graph[node][0] != color:
                  twoColor = False
            # print (queue)
            # flatten list and take the set of all nighbors in the next layer
            queue = list(set(flatten(queue)))
            # print (queue)
            color = switchColor(color)      
   return (conComp, twoColor)

def main():
   graphDict = createList()
   # print (graphDict)
   connected, twoColor = colorGraph(graphDict)
   # print (graphDict)
   print "Connected Components:", connected
   print "Two Colorable?", twoColor

if __name__ == '__main__':
   main()

