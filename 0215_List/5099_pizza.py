import sys
sys.stdin = open('5099_input.txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 화덕의 크기, M: 피자 개수
    Ci = deque(map(int, input().split()))    # Ci: M개의 피자에 뿌려진 치즈의 양
    # [7, 2, 6, 5, 3]
    # [5, 9, 3, 9, 9, 2, 5, 8, 7, 1]
    # [20, 4, 5, 7, 3, 15, 2, 1, 2, 2]

    q = deque([0] * N)
    front = rear = 0

    if q[0] == 0 and len(Ci) != 0:
        C = Ci.popleft()
        q[rear] = C
        rear += 1

    # for _ in range(N):
    #     C = Ci.popleft()
    #     q[rear] = C
    #     rear += 1
    #     if rear == N:
    #         for _ in range(N):
    #             n = q.popleft()
    #             q.append(n//2)

    print(q)








