# Given an array of positive integers. Your task is to find the leaders in the array.
# Note: An element of array is leader if it is greater than or equal to all the elements to its right side. 
# Also, the rightmost element is always a leader. 

for i in range(int(input())):
    
    n = int(input())
    lst = list(map(int, input().split()))
    mx = lst[-1]
    arr=[mx]
    
    if len(lst)==1:
        print(arr)
    
    else:
        for i in range(n-2,-1,-1):
            
            if lst[i]>=mx:
                arr.append(lst[i])
                
            mx = max(lst[i],mx)
            
        print(*(arr[::-1]))     
            