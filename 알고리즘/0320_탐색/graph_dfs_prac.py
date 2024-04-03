import sys
sys.stdin = open('18459_input.txt')


V, E = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(E)]

for i in range(E):
    graph[arr[i*2]].append(arr[(i*2)+1])
    graph[arr[(i*2)+1]].append(arr[i*2])

visited = [0]*E
path = []

def dfs(now):
    for to in graph[now]:
        if visited[to]:
            continue
        visited[to] = 1
        path.append(to)
        dfs(to)

visited[1] = 1
path.append(1)
dfs(1)

print('#1 ', end='')
for i in range(len(path)):
    if i < len(path)-1:
        print(path[i], '-', sep='', end='')
    else:
        print(path[i], sep='', end='')
