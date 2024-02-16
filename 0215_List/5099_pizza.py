import sys
sys.stdin = open('5099_input.txt')

# 치즈 양에 따라 굽는 시간 다르므로, 꺼내는 순서 다르게 됨
# 피자 번호는 1~M
# 피자는 1번 위치에서 넣거나 뺄 수 있음
# 원형 큐!!!

class cQueue:
    def __init__(self, size):
        self.front = 0
        self.rear = 0
        self.cQ = [0] * (size+1)        # front 위치를 비워두기 위해 +1

    def Qpeek(self):
        return self.cQ[(self.front+1) % len(self.cQ)]     # 원형큐이므로 인덱스 범위를 맞추기 위해 Q 사이즈만큼 나머지 값을 인덱스로 사용용

    def is_full(self):
        return self.front == (self.rear+1) % len(self.cQ)

    def is_empty(self):
        return self.front == self.rear

    def enQ(self, value):
        if self.is_full():
            print('Full!!!')
            return
        else:
            self.rear = (self.rear+1) % len(self.cQ)
            self.cQ[self.rear] = value

    def deQ(self):
        if self.is_empty():
            print('Empty!!!')
            return
        else:
            value = self.Qpeek()
            self.front = (self.front+1) % len(self.cQ)
            self.cQ[self.front] = 0
            return value

# from collections import deque

T = int(input())
for tc in range(1, T+1):
    # N: 화덕의 크기, M: 피자 개수
    N, M = map(int, input().split())
    pizza_list = list(map(int, input().split()))    # Ci: M개의 피자에 뿌려진 치즈의 양
    # [7, 2, 6, 5, 3]
    # [5, 9, 3, 9, 9, 2, 5, 8, 7, 1]
    # [20, 4, 5, 7, 3, 15, 2, 1, 2, 2]

    q = cQueue(N)       # 빈 화덕
    # 빈 화덕에 피자 넣기
    for idx in range(N):
        q.enQ([pizza_list[idx], idx+1]) # Queue에 [치즈양, 피자번호]를 넣어서 관리

    p_idx = idx     # 들어간 마지막 피자 index 저장
    result = 0

    while not q.is_empty():
        # 피자를 꺼낸다. (치즈//2)
        pizza = q.deQ()
        pizza[0] = pizza[0] // 2
        result = pizza[1]
        # 피자 치즈가 남아 있다면 그대로 enQ
        # 피자 치즈가 남아있지 않다면 다음 피자 enQ
        if pizza[0]:
            q.enQ(pizza)
        else:
            p_idx += 1
            if p_idx < M:
                q.enQ([pizza_list[p_idx], p_idx+1])
            # 다음 피자가 없다면 skip

    print(f'#{tc} {result}')


    # q = deque([0] * N)
    # front = rear = 0

    # if q[0] == 0 and len(Ci) != 0:
    #     C = Ci.popleft()
    #     q[rear] = C
    #     rear += 1

    # while True:
    #     for _ in range(N):
    #         C = Ci.popleft()
    #         q[rear] = C
    #         rear += 1
    #         if rear == N:
    #             for _ in range(N):
    #                 n = q.popleft()
    #                 q.append(n//2)
    #     if len(Ci) == 0:
    #         break
    #
    # print(q)











