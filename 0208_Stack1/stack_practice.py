import sys
sys.stdin = open('stack_input.txt')

def dfs(i): # 시작: i, 마지막: V
    visited[i] = 1   # 방문 표시
    print(i)        # 출력
    # i에 인접하고 방문 안한 w가 있으면
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)

T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge_list = list(map(int, input().split()))

    # 정점 번호대로 빈 리스트 생성
    # [[], [], [], [], [], [], [], []]
    adj_list = [[] for _ in range(V + 1)]

    # adj_list[0] = [1]

    for idx in range(E):
        start = edge_list[idx * 2]
        end = edge_list[idx * 2 + 1]
        adj_list[start].append(end)
        adj_list[end].append(start)

    visited = [0] * (V + 1)

    for i in range(V + 1):
        print(adj_list[i])