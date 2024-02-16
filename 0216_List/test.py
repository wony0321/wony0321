'''
V E: V 1~V번까지 V개의 정점. E개의 간선
E개의 간선 정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

import sys
sys.stdin = open('18459_input.txt')

def bfs(s, N):  # 시작정점 s, 노드개수 N
    q = []  # 큐
    ans_lst = []
    visited = [0] * (N+1)  # visited (-1로 초기화하면 visited[s] 0으로 시작도 가능)
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:        # 큐가 비워질때까지...(남은 정점이 있으면)
        t = q.pop(0)
        # t에서 할일...
        ans_lst.append(t)
    # return ans_lst
        for i in adjl[t]:   # t에 인접인 애들 하나씩 꺼내볼래?(인접인 정점)
            if visited[i]==0:   # 방문하지 않은 정점이면 (if not visited[i]로도 표현 가능)
                q.append(i)
                visited[i] = 1 + visited[t]
    return ans_lst

T = 1
for tc in range(1, T+1):
    # 정점의 개수 V, 간선의 개수 E
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))

    print(arr)

    # 인접리스트
    adjl = [[] for _ in range(V+1)]

    # for i in range(0, E*2, 2):
    #     n1, n2 = arr[i], arr[i+1]
    # 위와 같이 표현해도 됨
    for i in range(E):
        # 2개의 쌍을 읽어내는 방법
        n1, n2 = arr[i*2], arr[i*2+1]
        adjl[n1].append(n2)
        adjl[n2].append(n1) # 무향그래프(방향 없어서 양쪽 다 표시)

    print(adjl)

    # print(f'#{tc}', *bfs(1, V))