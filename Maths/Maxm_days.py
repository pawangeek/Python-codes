for i in range(int(input())):
    for j in range(int(input())):
        
        if j == 0:
            r = int(input())
        
        else:
            r = max(r,int(input()))
        
    print(r)