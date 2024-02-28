import sys
sys.stdin = open('2817_input.txt')


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(1<<N):
        for j in range(N):
            if i & (1<<j):
                print(A[j], end='')
        print()
    print()