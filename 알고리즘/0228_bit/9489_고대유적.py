import sys
sys.stdin = open('9489_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    len_data = []

    for i in range(N):
        cnt_w = 0
        for j in range(M):
            if data[i][j] == 1:
                cnt_w += 1
            else:
                if cnt_w >= 2:
                    len_data.append(cnt_w)
                cnt_w = 0
        if cnt_w >= 2:
            len_data.append(cnt_w)

    for j in range(M):
        cnt_h = 0
        for i in range(N):
            if data[i][j] == 1:
                cnt_h += 1
            else:
                if cnt_h >= 2:
                    len_data.append(cnt_h)
                cnt_h = 0
        if cnt_h >= 2:
            len_data.append(cnt_h)

    print(f'#{tc} {max(len_data)}')