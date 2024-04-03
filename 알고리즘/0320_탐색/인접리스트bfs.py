# 인접 리스트 BFS: 이차원 배열
# 따로 딕셔너리랑 deque도 써보기
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3],
]

# 갈 수 있는 곳 다 가기
# 방문 순서대로 다음 노드 찾음(먼저 방문하면 먼저 다음 노드로 감(FIFO=queue))

# 1) 리스트로 queue를 구현할 수도 있고, 2) deque 활용한 queue 사용할 수도 있음

visited = [0] * 5

def bfs(start):
    # 재귀가 아니어서 안에 써도 OK

    # queue = deque()
    # 시작 노드를 큐에 추가 + 방문 표시
    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        # 갈 수 있는 곳을 체크
        for to in graph[now]:
            if visited[to]:
                continue
            visited[to] = 1
            queue.append(to)

bfs(0)