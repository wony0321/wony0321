import sys
sys.stdin = open('1260.txt')

def DFS(s):
    for to in graph[s]:
        if visited[to]:



T = int(input())
for tc in range(1, T+1):
    N, M, V = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(M)]
    visited = [0]*N
    path = []

