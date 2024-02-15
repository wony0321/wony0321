'''
3
1 2 3
4 5 6
7 8 9


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
arr2 = [[0]*N for _ in range(N)]
print(arr2)
# arr3 = [[0]*N]*N
# print(arr3)
# arr3[0][0] = 1
# print(arr3)
# 주석 처리된 부분처럼 저어얼대 하지 말기
'''

'''
# 오른쪽, 아래쪽, 왼쪽, 위쪽
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 5
arr = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                print(arr[ni][nj], end=' ')
        print()

# i = 3
# j = 4
#
# for k in range(4):
#     ni = i + di[k]
#     nj = j + dj[k]
#     print(ni, nj)


# N = 5
# arr = [[0]*N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#             ni, nj = i+di, j+dj
#             if 0 <= ni < N and 0 <= nj < N:
#                 print(arr[ni][nj])
'''
# arr = [1, 2, 3]
#
# n = len(arr)
# -7 -5 2 3 8 -2 4 6 9
'''
def f(arr, N):
    for i in range(1, 1 << N):  # 1<<n는 2의 n 제곱 의미(비트의 개수 의미)
        s = 0  # 합
        for j in range(N):
            if i & (1 << j):
                s += arr[j]
                # print(arr[j], end=", ")
        if s == 0:
            return True
    return False


N = int(input())
arr = list(map(int, input().split()))
print(f(arr, N))
'''

'''
import sys
sys.stdin = open('input.txt')

N = int(input())  # 2차원 리스트의 크기

arr = []
for _ in range(N):  # N번 반복
    arr.append((list(map(int, input().split()))))
print(arr)

# [표현식 for _ in range(N)]

arr2 = [list(map(int, input().split())) for _ in range(N)]  # [표현식, 표현식, list(map(int, input().split()))]
print(arr2)
'''
'''
import sys
sys.stdin = open('input.txt')


array = list(map(int, input().split()))

for i in range(3):
    for j in range(4):
        print(array[i][j])
'''

'''
# 비트의 자리 수 = arr에서 사용하는 각 요소
arr = ['a', 'b', 'c', 'd']
N = len(arr)

# arr 에 대한 모든 경우의 수
for i in range(1<<N):  # 모든 부분 집합을 구하기 위한 반복 -> 2^4는 모두 4비트로, 0~15까지 표현할 수 있음
    # 부분 집합을 저장하기 위한 임시 리스트
    temp_lst = []
    # arr의 idx
    for j in range(N):  # j : 해당 비트의 자리가 1인지 확인하기 위해 (shift를 하는 역할)
        print('='*30)
        # i: 모든 경우의 수 중, i번째
        # 1<<j: arr의 j번째 요소의 비트
'''