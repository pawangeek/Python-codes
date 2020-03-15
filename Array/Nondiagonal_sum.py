# Task : we have to find the sum of non diagonal elements
# Approach : just not take elements have i==j(diagonal) and i==(n-j)(off-diagonal)

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
d=[]

for i in range(len(arr)):
    for j in range(len(arr)):
        if i==j:
            continue
        elif (i==(len(arr)-j-1)):
            continue
        else:
            d.append(arr[i][j])
        
print(sum(d))