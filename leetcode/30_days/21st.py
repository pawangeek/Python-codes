# Leftmost Column with at Least a One
# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/


#n, m = len(binaryMatrix), len(binaryMatrix[0])
n, m = binaryMatrix.dimensions()
row = 0
col = m-1
        
# last column where we found 1, default case is -1
lastOneCol = -1
        
while 0 <= row < n and col >= 0:
            
    #value = binaryMatrix[row][col] 
    value = binaryMatrix.get(row, col)
            
    # one found - update lastOneCol, go left
    if value == 1:
        lastOneCol = col
        col -= 1
                
    # zero found - go down    
    else:
        row += 1
                
# return last column where we met 1
print (lastOneCol)