import sys
sys.stdin = open('4837_input.txt')

T = int(input())

# 숫자 1~12를 가진 집합 A를 리스트로 만듦
A = []
for num in range(1, 13):
    A.append(num)

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # N은 원소의 수, K는 원소의 합

    cnt = 0
    for i in range(1, 1 << 12):
        s = 0  # 합
        num_lst = []
        for j in range(12):
            if i & (1 << j):
                s += A[j]
                num_lst.append(A[j])
        if len(num_lst) == N and s == K:
            cnt += 1

    print(f'#{tc} {cnt}')