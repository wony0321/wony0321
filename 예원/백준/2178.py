from collections import deque
import sys
sys.stdin = open('2178.txt')

def dfs(start, cnt):
    queue = deque([start])

    while queue:
        i, j = queue.popleft()
        if i==N-1 and j==M-1:
            break
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M and board[ni][nj]==1 and visited[ni][nj] ==0:
                cnt += 1
                visited[ni][nj] = 1
                queue.append([ni, nj])
    return cnt
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸
    board = [list(map(int, input())) for _ in range(N)]
    di = [1, 0, -1,0]
    dj = [0, 1, 0,-1]

    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    cnt = 1

    ans = dfs([0, 0], cnt)
    print(ans)