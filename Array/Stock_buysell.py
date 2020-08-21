# Approach : Peak and valley problem

for i in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    i = 0
    lst = []
    
    while i<(n-1):
        
        while i<(n-1) and arr[i+1]<=arr[i]:
            i+=1
            
        if i==(n-1):
            break
        
        buy = i
        i+=1
        
        while i<n and arr[i]>=arr[i-1]:
            i+=1
            
        sell = i-1
        
        lst.append("(%d %d)" %(buy, sell))
        
    print(*(lst)) if lst else print("No Profit")
        