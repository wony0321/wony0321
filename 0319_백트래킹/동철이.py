import sys
sys.stdin = open('1865_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = [[] for _ in range(N)]

    for turn in range(N):
        arr = list(map(int, input().split()))
        for i in range(N):
            work[i].append((turn+1, arr[i]))
    print(work)


