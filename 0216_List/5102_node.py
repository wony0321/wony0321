import sys
sys.stdin = open('5102_input.txt')

def bfs(s, N, G):  # 시작정점 s, 노드개수 N
    q = []  # 큐
    visited = [0] * (N + 1)  # visited (-1로 초기화하면 visited[s] 0으로 시작도 가능)
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:  # 처리 안 된 정점이 남아 있으면
        t = q.pop(0) # 처리할 정점 디큐
        if t == G: # G라는 정점까지의 최단 거리 필요한 것
            # 최단 경로 간선 수
            return visited[t]-1     # 시작 정점이 1부터 시작하므로, 1 빼주어야함
        for i in adjl[t]:       # t의 인접정점이
            if visited[i]==0:           # 인큐되지 않았으면(처리된 적이 없으면)
                q.append(i)
                visited[i] = visited[t]+1   # 하나 더 왔다!
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 인접리스트
    adjl = [[] for _ in range(V + 1)]

    # for i in range(0, E*2, 2):
    #     n1, n2 = arr[i], arr[i+1]
    # 위와 같이 표현해도 됨
    for i in range(E):
        # 2개의 쌍을 읽어내는 방법
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)  # 무향그래프(방향 없어서 양쪽 다 표시)

    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, V, G)}')