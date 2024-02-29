import sys
sys.stdin = open('4861_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    str_lst = [list(map(str, input().split())) for _ in range(N)]

    print(str_lst)

    for i in range(N):
        for s in str_lst[i]:
            reverse_str = s[::-1]
            if s == reverse_str:
                print(1)
            else:
                continue

    for i in range(N):
        for s in str_lst[i]:
            reverse_str = s[::-1]
            if s == reverse_str:
                print(1)
            else:
                continue