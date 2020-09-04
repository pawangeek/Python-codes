graph = [[1, 4, 5, 6], [], [0, 1, 2, 5], [0, 2, 4], [0, 1, 4], [1, 2, 3, 6], [2, 3]]
n = len(graph)
color = {}

def dfs(position):

    print(color)
    for i in graph[position]:

        if i in color:
            if color[i]==color[position]:
                return False

        else:
            color[i] = 1-color[position]
            if not dfs(i):
                return False

    return True

f=0

for i in range(n):

    if i not in color:
        color[i]=0
        if not dfs(i):
            f=1
            break
    
print(1) if f==0 else print(0)


