# Using DFS (TLE)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

def dfs(graph, visited, i, cnt):
    
    visited[i] = True
    
    for j in graph[i]:
        if visited[j] is False:
            cnt[0] += 1
            dfs(graph, visited, j, cnt)
            
    return cnt

for _ in range(m):

    arr = list(map(int, input().split()))
    size = arr[0]

    if size>0:
        for i in range(1, size):
            graph[arr[i]].append(arr[i+1])
            graph[arr[i+1]].append(arr[i])
            
ans = []

for i in range(1, n+1):
    
    visited = [False]*(n+1)
    cnt = dfs(graph, visited, i, [1])
    
    ans.append(cnt[0])

print(*(ans))

# Using DSU (Acc)

def find(a):
    if parent[a]<0:
        return a
    
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    x = find(a)
    y = find(b)

    if x==y:
        return

    parent[x] += parent[y]
    parent[y] = x

n, m = map(int, input().split())
parent = [-1]*(n+1)

for _ in range(m):

    arr = list(map(int, input().split()))
    size = arr[0]

    for i in range(1, size):
        union(arr[i], arr[i+1])

ans = []

for i in range(1, n+1):
    ans.append(abs(parent[find(i)]))

print(*ans)