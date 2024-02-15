import sys
sys.stdin = open('1210_input.txt')

T = 10

for tc in range(1, T+1):
    T_num = int(input())
    N = 100
    data = [list(map(int, input().split())) for _ in range(N)]

    # 2 찾기
    start_j = 0
    for j in range(N):
        if data[99][j] == 2:
            start_j = j
    # print(start_j) #57
    start = [99, start_j]

    # 갈 수 있는 방향 델타로 설정
    di = [0, 0, -1]  # [왼쪽 행, 위 행, 왼쪽 행]
    dj = [-1, 1, 0]  # [오른 열, 위 열, 왼쪽 열]

    # 본인이 지나온 곳을 0으로 바꾸기

    while start[0] > 0:
        for k in range(3):  # 델타 이용해서 배열 탐색하기 위한 for 문
            ni = start[0] + di[k]  # 0 들어오면 오른쪽, 1 들어오면 위쪽, 2 들어오면 왼쪽
            nj = start[1] + dj[k]  # 0 들어오면 오른쪽, 1 들어오면 위쪽, 2 들어오면 왼쪽
            if 0 <= ni < N and 0 <= nj < N:
                if data[ni][nj] == 1:
                    # 이동하기 전에 다시 되돌아 가지 않도록 표시
                    data[ni][nj] = 3
                    start[0], start[1] = ni, nj
                    # 1이 아닌 값을 넣어 다시 돌아가는 것을 방지!!
                    # 이렇게 지나온 곳 0으로 바꿔도 가능
                    # data[ni][nj] = 0
                    break # 불필요한 연산을 줄이기 위해
    print(f'#{T_num} {start[1]}')