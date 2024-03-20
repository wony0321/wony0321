from collections import deque
import sys
sys.stdin = open('18459_input.txt')


V, E = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(E)]

for i in range(E):
    graph[arr[i*2]].append(arr[(i*2)+1])

visited = [0]*(V+1)

print(f'#1', end=' ')
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for to in graph[now]:
            if visited[to]:
                continue
            visited[to] = 1
            queue.append(to)
bfs(1)

