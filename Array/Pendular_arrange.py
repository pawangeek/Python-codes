# Task : To arrange the given array in pendulam style 
# Minimum at middle than left right continue

t = int(input())

while t:
    p = int(input())
    arr = list(map(int,input().split()))
    narr = arr.copy()
    arr.sort()
    
    if p%2==1:
        narr[int(p/2)],u=arr[0],1
        for i in range(1,int(p/2)+1):

            narr[(int(p/2))+i] = arr[u]
            narr[(int(p/2))-i] = arr[u+1]

            u=u+2
    
    else:
        narr[int((p-1)/2)],u,narr[p-1]=arr[0],1,arr[p-1]
        for i in range(1,int((p)/2)):

            narr[(int((p-1)/2))+i] = arr[u]
            narr[(int((p-1)/2))-i] = arr[u+1]

            u=u+2
   
    for i in narr:
        print(i,end=' ')
        
    print()

    t-=1