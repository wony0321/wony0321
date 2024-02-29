def f(i, k):
    global min_v
    global cnt
    cnt += 1
    if i==k:
        print(*P)
        s = 0   # 선택한 원소의 합
        for j in range(k):  # j행에 대해
            s += arr[j][P[j]]   # j행에서 P[j] 열을 고른 경우의 합 구하기
        if min_v > s:
            min_v = s  # 자리 맞추는 것 중요
    else:
        for j in range(i, k):   # P[i]자리에 올 원소 P[j] 결정
            P[i], P[j] = P[j], P[i]     # P[i] <-> P[j]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]     # 교환전으로 원상 복구

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
cnt = 0
f(0, N)
print(min_v, cnt)

'''
0 1 2   0번 행에서는 0번, 1번 행에서는 1번, 2번 행에서는 2번 고름
0 2 1   0번 행에서는 0번, 1번 행에서는 2번, 2번 행에서는 1번 고름
1 0 2
1 2 0
2 1 0
2 0 1
8
'''

'''
9 326
'''