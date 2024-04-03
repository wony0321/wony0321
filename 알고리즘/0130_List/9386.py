import sys
sys.stdin = open('9386_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input()))

    num_lst.append(0)
    cnt = 0
    new_lst = []
    max = 0

    for num in num_lst:
        if num == 0:
            new_lst.append(cnt)
            cnt = 0
        elif num == 1:
            cnt += 1

    for i in range(len(new_lst)):
        if max <= new_lst[i]:
            max = new_lst[i]

    print(f'#{tc} {max}')