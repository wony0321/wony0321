import sys
sys.stdin = open('5105_input.txt')

def bfs(i, j):  # 시작 행, 시작 열
    q = []  # 큐
    visited = [[0] * N for _ in range(N)]  # N * N의 2차원 리스트 (새로운 지도)
    q.append([i, j])  # 방문할 곳 넣기
    visited[i][j] = 1  # 방문 처리
    while q:        # 큐가 비워질때까지
        # 언패킹: r, c = [i, j]
        r, c = q.pop(0)     # t = q.pop(0), t[0] = i / t[1] = j
        # t에서 할 일 -> 이동할 수 있는 좌표 찾기
        for idx in range(4):
            ni = r + di[idx]
            nj = c + dj[idx]
            if 0<=ni<N and 0<=nj<N:
                if maze_info[ni][nj] == 0 and visited[ni][nj] == 0:
                    q.append([ni, nj])
                    visited[ni][nj] = 1 + visited[r][c]
                elif maze_info[ni][nj] == 3:
                    return visited[r][c] - 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze_info = [list(map(int, input())) for _ in range(N)]

    # 우, 좌, 하, 상
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    for i in range(N):
        for j in range(N):
            if maze_info[i][j] == 2:
                print(f'#{tc} {bfs(i, j)}')
                break
