# import sys
# sys.stdin = open('2578_input.txt')

bingo = [list(map(int, input().split())) for _ in range(5)]
num_arr = []
for _ in range(5):
    num_arr.extend(list(map(int, input().split())))

for turn in range(len(num_arr)):
    for i in range(5):
        for j in range(5):
            if num_arr[turn] == bingo[i][j]:
                bingo[i][j] = 0
    bingo_cnt = 0
    cnt_d_1 = 0
    cnt_d_2 = 0
    for c in range(5):
        cnt_w = 0
        cnt_h = 0
        if bingo[c][c] == 0:
            cnt_d_1 += 1
        # 대각선 표현에 대해서 생각해봅시다.
        if bingo[c][4-c] == 0:
            cnt_d_2 += 1
        for r in range(5):
            if bingo[c][r] == 0:
                cnt_w += 1
            if bingo[r][c] == 0:
                cnt_h += 1
        # if 문에서 or이 어떤 작용을 하는지 생각해봅시다.
        if cnt_h >= 5:
            bingo_cnt += 1
        if cnt_w >= 5:
            bingo_cnt += 1
    # if 문에서 or이 어떤 작용을 하는지 생각해봅시다.
    if cnt_d_1 >= 5:
        bingo_cnt += 1
    if cnt_d_2 >= 5:
        bingo_cnt += 1
    # 빙고 조건에 대해서 생각해봅시다.
    if bingo_cnt >= 3:
        print(turn+1)
        break