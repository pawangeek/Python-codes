# Task : to find element in rortated array
# Complexity : O(n) since index operation is of O(n)

t = int(input())

for i in range(t):
    s = int(input())
    arr = list(map(int,input().split()))   
    e = int(input())
    
    try:
        print(arr.index(e))
    except:
        print(-1)