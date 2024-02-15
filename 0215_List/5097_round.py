import sys
sys.stdin = open('5097_input.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: arr 길이, M: 작업 횟수
    arr = deque(map(int, input().split()))

    for _ in range(M):
        num = arr.popleft()
        arr.append(num)

    print(f'#{tc} {arr.popleft()}')

