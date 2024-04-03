import sys
sys.stdin = open('1225_input.txt')

from collections import deque


T = 10
for tc in range(1, T+1):
    N = 8
    test_num = int(input())
    arr = deque(map(int, input().split()))

    while True:
        for i in range(1, 6):
            n = arr.popleft()
            if n-i > 0:
                arr.append(n-i)
            else:
                arr.append(0)
                break
        if arr[-1] == 0:
            break

    print(f'#{tc}', *arr)
    # print(arr)