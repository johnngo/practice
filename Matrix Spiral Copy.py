def spiral_copy(inputMatrix):
    numRows = len(inputMatrix)    #4
    numCols = len(inputMatrix[0]) #5
    print(numCols)
    
    topRow = 0
    btmRow = numRows - 1  #3
    leftCol = 0
    rightCol = numCols - 1 #4
    result = []

    while (topRow <= btmRow and leftCol <= rightCol):
        # copy the next top row
        for i in range(leftCol,rightCol+1):
            result.append(inputMatrix[topRow][i])
        topRow +=1

        # copy the next right hand side column
        for i in range(topRow , btmRow+1):
            result.append(inputMatrix[i][rightCol])
        rightCol -=1

        # copy the next bottom row
        if (topRow <= btmRow):
            for i in range(rightCol,leftCol-1,-1):
                result.append(inputMatrix[btmRow][i])
            btmRow -=1

        # copy the next left hand side column
        if (leftCol <= rightCol):
            for i in range(btmRow,topRow-1,-1):
                result.append(inputMatrix[i][leftCol])
            leftCol +=1

    return result
  
#inputMatrix  = [ [1,    2,   3,  4,    5], 
   #              [6,    7,   8,  9,   10], 
    #             [11,  12,  13,  14,  15], 
     #            [16,  17,  18,  19,  20] ]

#spiralCopy(inputMatrix)