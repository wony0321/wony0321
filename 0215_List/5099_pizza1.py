import sys
sys.stdin = open('5099_input.txt')

T = int(input())
for tc in range(1, T+1):
    # N: 화덕의 크기, M: 피자 개수
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    q = [0]*N

    while Ci:
        for i in range(N):



