n, m, k = map(int, input().split())
graph = []

for _ in range(m):
    u, v, w = map(int, input().split())
    graph.append((u, v, w))

if k>0:
    flour = set(map(int, input().split()))

minw = 10**10,-1

if k==0:
    print(-1)

else:
    for i in range(graph):
        u, v, w = graph[i]

        if u in flour:
            if v not in flour:
                minw = min(minw, w)

        if v in flour:
            if u not in flour:
                minw = min(minw, w)

    print(-1) if minw==10**10 else print(minw)

    