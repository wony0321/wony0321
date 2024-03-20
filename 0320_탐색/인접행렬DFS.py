# 인접 행렬 DFS: 재귀 버전
# 재귀 배우기 전에는 stack 활용함
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
]

# 한 번 방문한 곳은 다시 방문할 수 없도록 visited 활용
visited = [0] * 5
path = []

def dfs(now):
    # 기저 조건
    # 지금 문제에서는 없다!

    # 다음 재귀 호출 전
    # 재귀 호출 후에 출력
    # visited[now] = 1
    # path.append(now)
    # print(now, end=' ')

    # 다음 재귀 호출
    # dfs: 현재 노드에서 다른 노드들을 확인 (후보군) => 다른 노드들이므로 '반복문' 사용
    for to in range(5):
        # 갈 수 없다면 pass
        if graph[now][to] == 0:
            continue

        # 이미 방문했다면 pass
        if visited[to]:
            continue

        # 가기 전에 작업 (이게 더 선호됨)
        # 다음에 갈 때 작업하므로 출발점은 저장이 안됨
        visited[to] = 1
        path.append(to)
        dfs(to)
    # 돌아왔을 때 작업
# 출발점 초기화
visited[0] = 1
path.append(0)
dfs(0)
print(path)