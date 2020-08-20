for i in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    s,f = set(),0
    
    for i in range(n):
        
        if (arr[i]*arr[i] in s):
            f=1
            break
            
        for j in range(i+1, n):
            s.add(arr[i]*arr[i] + arr[j]*arr[j])
            
    print("Yes") if f==1 else print("NO") 