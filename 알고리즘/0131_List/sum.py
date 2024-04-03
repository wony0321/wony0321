import sys
sys.stdin = open('1209_sum_input.txt')

T = 10

for tc in range(1, T+1):
    tc_num = int(input()) # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_num = 0

    for i in range(100):
        x_sum = 0
        # y_sum = 0
        for j in range(100):
            x_sum += arr[i][j]
            # y_sum += arr[j][i]
        if x_sum > max_num:
            max_num = x_sum
        # if y_sum > max_num:
        #     max_num = y_sum

    for j in range(100):
        y_sum = 0
        for i in range(100):
            y_sum += arr[i][j]
        if y_sum >= max_num:
            max_num = y_sum

    z1 = 0
    z2 = 0
    for i in range(100):
        z1 += arr[i][i]
        z2 += arr[i][99-i]
    if z1 >= max_num:
        max_num = z1
    elif z2 >= max_num:
        max_num = z2

    print(f'#{tc} {max_num}')

