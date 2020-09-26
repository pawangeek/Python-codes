# Have to make a graph -> Directed tree (one direction)

for _ in range(int(input())):

    n = int(input())

    graph = [0]*(n+1)
    count = 0

    for i in range(n-1):
        u, v = list(map(int, input().split()))
        graph[v]+=1
    
    for i in range(1,len(graph)):
        if graph[i]>1:
            while(graph[i] != 1):
                count+=1
                graph[i]-=1
                
    print(count)
