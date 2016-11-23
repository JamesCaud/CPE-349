"""
James Caudill
lab4 - Dynamic Programming
CPE 349 - Migler
"""

import sys


"""
initGTS creates a 3d array the size the GTS 
(row - row0 + 1, col - col0 + 1)
"""
def initGTS(row, col):
    return [[[0, ''] for i in range(col)] for i in range(row)]


"""
initTGame creates a 2d array the size of the GTS 
with the values of the orig table 
"""
def initTGame(game, row, col, row0, col0):
    TGame = [[0 for i in range(col - col0 + 1)] for i in range(row - row0 + 1)]
    for i in range(1, row - row0 + 1):
        for j in range(1, col - col0 + 1):
                TGame[i][j] = game[row0 - 1 + i][col0 - 1 + j]
    return TGame    


"""
findBestGTS loops through all starting positions and finds the best starting point
"""
def findBestGTS(game, row, col):
    maxNum, sumVertex = findGTS(game,row,col,0,0)
    
    print (maxNum, sumVertex)
    return maxNum, sumVertex


"""
findGTS finds the greatest travel sum only going down or right
game is a list of list aka the 2d array
row and col are the total rows and cols of the game board
row0 and col0 are the starting points for the algorithm
"""
def findGTS(game, row, col, row0, col0):
    newRow = row - row0 + 1
    newCol = col - col0 + 1
    GTS = initGTS(newRow, newCol)
    TGame = initTGame(game, row, col, row0, col0)

    for i in range(1, newRow):
        for j in range(1, newCol):
            if i == 1 and j == 1:
                GTS[i][j][0] = TGame[i][j]
                #GTS[i][j][1] += "{}, {}\n".format(i,j)
            elif GTS[i-1][j][0] >= GTS[i][j-1][0] and GTS[i-1][j][0] + TGame[i][j] >= TGame[i][j]:
                GTS[i][j][0] = GTS[i-1][j][0] + TGame[i][j]
                #GTS[i][j][1] += GTS[i-1][j][1] + "{}, {}\n".format(i,j)
            elif GTS[i][j-1][0] >= GTS[i-1][j][0] and GTS[i][j-1][0] + TGame[i][j] >= TGame[i][j]:
                GTS[i][j][0] = GTS[i][j-1][0] + TGame[i][j]
                #GTS[i][j][1] += GTS[i][j-1][1] + "{}, {}\n".format(i,j)
            else:
                GTS[i][j][0] = TGame[i][j]
                #GTS[i][j][1] += "{}, {}\n".format(i,j)

                
    maxVal = GTS[i][j][0]
    pathHomeSt = (i,j)
    #print (GTS)
    
    for i in range(1, newRow-1):
        if GTS[i][newCol - 1][0] >= maxVal:
            maxVal = GTS[i][newCol - 1][0]
            pathHomeSt = (i, newCol - 1)
    for j in range(1, newCol -1):
        if GTS[newRow - 1][j][0] >= maxVal:
            maxVal = GTS[newRow - 1][j][0]
            pathHomeSt = (newRow - 1, j)
    
    print (maxVal, pathHomeSt)
    print (GTS[pathHomeSt[0]][pathHomeSt[1]][1])

    return maxVal, pathHomeSt
    

def main():
    GAME_COL = 0
    GAME_ROW = 0
    GAME_BOARD = []
    
    with open(sys.argv[1], 'r') as inFile:
        GAME_ROW = int(inFile.readline())
        GAME_COL = int(inFile.readline())
        for line in inFile:
            GAME_BOARD.append([int(i) for i in line.split()])
    
    #print (GAME_BOARD)
    
    command = input('Where to start? OR Best: ')
    print (command)
    if (command == 'B'):
        findBestGTS(GAME_BOARD, GAME_ROW, GAME_COL)
    else:
        command = [int(i) for i in command.split()]
        i, j = command[0], command[1]
        findGTS(GAME_BOARD, GAME_ROW, GAME_COL, i, j)
    
    
if __name__ == '__main__':
    main()
