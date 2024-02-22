import sys
sys.stdin = open('5186_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    ans_lst = []
    while N > 0:
        ans_lst.append(int(N * 2))
        N = N*2 - ans_lst[-1]
    if len(ans_lst) >= 13:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc}', end=' ')
        print(*ans_lst, sep='')


