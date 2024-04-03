import sys
sys.stdin = open('5789_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    counts = [0] * N

    for i in range(1, Q+1):
        Li, Ri = list(map(int, input().split()))
        for nums in range(Li, Ri+1):
            counts[nums-1] = i

    print(f'#{tc}', *counts)