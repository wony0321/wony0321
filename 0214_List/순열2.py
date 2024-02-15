def f(i, k, s):     # i-1까지 선택한 원소의 합
    global min_v
    global cnt
    cnt += 1
    if i==k:
        # print(*P)
        if min_v > s:
            min_v = s  # 자리 맞추는 것 중요
    elif s >= min_v:
        return
    else:
        for j in range(i, k):   # P[i]자리에 올 원소 P[j] 결정
            P[i], P[j] = P[j], P[i]     # P[i] <-> P[j]
            f(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]     # 교환전으로 원상 복구

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
cnt = 0
f(0, N, 0)
print(min_v, cnt)

'''
9 181
'''

# 가지치기의 효과는 경우의 수가 많으면 많을 수록 높아짐