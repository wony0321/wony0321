import sys
sys.stdin = open('9367_input.txt')

T = int(input())
for tc in range(1, T+1):
    # 당근의 개수
    N = int(input())
    # 당근의 크기 (1~10)
    C = list(map(int, input().split()))

    max_cnt = 0
    cnt = 1
    for i in range(N-1):
        if C[i] < C[i+1]:
            cnt += 1
        else:
            cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')