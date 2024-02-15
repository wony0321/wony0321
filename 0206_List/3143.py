import sys
sys.stdin = open('3143_input.txt')

T = int(input())
for tc in range(1, T+1):
    str_a, str_b = map(str, input().split())
    N = len(str_a)
    M = len(str_b)

    for a in range(N):
        