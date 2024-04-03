# 부분집합 출력
def f(i, k):
    if i==k:    # 모든 원소에 대해 결정하면
        ss = 0  # 부분집합 원소의 합
        for j in range(k):
            if bit[j]:  # bit[j]==1에서 ==1 생략 가능 -> 0 아니면 참
                        # A[j]가 포함된 경우
                print(A[j], end = ' ')
                ss += A[j]
        print(ss)
    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k)
        # bit[i] = 1
        # f(i+1, k)
        # bit[i] = 0
        # f(i+1, k)

# 부분집합 원소의 합이 t인 경우 출력
def f2(i, k, t):    # 여기서 t는 타겟값임
    if i==k:    # 모든 원소에 대해 결정하면
        ss = 0
        for j in range(k):
            if bit2[j]:  # bit[j]==1에서 ==1 생략 가능 -> 0 아니면 참
                        # A[j]가 포함된 경우
                ss += A2[j]
        if ss==t:
            for j in range(k):
                if bit2[j]:
                    print(A2[j], end=' ')
            print()
    else:
        for j in range(1, -1, -1):
            bit2[i] = j
            f2(i+1, k, t)

# 첫 합이 주어졌을 때의 target 값인 부분집합 찾기
def f3(i, k, s, t):
    global cnt
    cnt += 1
    if s==t:
        for j in range(k):
            if bit2[j]:
                print(A2[j], end=' ')
        print()
    elif i==k:  # 모든 원소를 고려했으나 s!=t
        return
    elif s > t:   # 고려한 원소의 합이 t보다 큰 경우
        return
    else:
        for j in range(1, -1, -1):
            bit2[i] = j
            f3(i + 1, k, s+A2[i]*j, t)
        # bit2[i] = 1
        # f3(i+1, k, s+A2[i], t)
        # bit2[i] = 0
        # f3(i+1, k, s, t)

N = 3
A = [1, 2, 3]
N2 = 10
A2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*N # bit[i]는 A[i]가 부분집합에 포함되는지 표시
bit2 = [0]*N2
# f(0, N)
# f2(0, N2, 10)
cnt = 0
f3(0, N2, 0, 10)
# print(f'cnt:', cnt)