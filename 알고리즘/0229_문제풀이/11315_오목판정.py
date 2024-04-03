import sys
sys.stdin = open('11315_input.txt')

def omok(y, x):
    # 아래, 오른쪽, 4시, 방향 2시 방향
    dy = [1, 0, 1, -1]
    dx = [0, 1, 1, 1]

    # 네 방향 탐색
    for bang in range(4):
        #기준 좌표에 돌이 있으면 cnt = 1부터 시작
        cnt = 1
        for power in range(1, 5):
            ny = y + (dy[bang]*power)
            nx = x + (dx[bang] * power)
            if not (0<=ny<N and 0<=nx<N):
                break
            if arr[ny][nx] == 'o':
                cnt += 1
            if cnt == 5:
                return True
    return False

def game_start():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                if omok(r, c):
                    return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    # result = game_start()
    # print(f'#{tc} {result}')


    di = [1, 0, 1, -1]
    dj = [0, 1, 1, 1]

    bingo = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                cnt = 0
                for n in range(5):
                    ni = i + di[k]*n
                    nj = j + dj[k]*n
                    if 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj] == 'o':
                            cnt += 1
                if cnt == 5:
                    bingo += 1
    if bingo:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

