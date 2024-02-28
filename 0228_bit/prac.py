# arr = ['A', 'B', 'C', 'D', 'E']
# dice = [1, 2, 3, 4, 5, 6]
# n = len(arr)
# path = []
#
# def get_count(tar):
#     cnt = 0
#     for i in range(n):
#         # 1 비트 1인지 아닌지 확인
#         if tar & 0x1:
#             cnt += 1
#         # right shift 비트 연산자 -> 오른쪽 끝 비트를 하나씩 제거
#         tar >>= 1
#     return cnt

# def run(lev, start):
#     if lev == n:
#         print(path)
#         return
#     for i in range(start, 5):
#         path.append(arr[i])
#         run(lev+1, i+1)
#         path.pop()

N = 3
path = []

def func(lev, start):
    if lev == N:
        print(path)
        return
    for i in range(start, 7):
        path.append(i)
        func(lev+1, i)
        path.pop()
func(0, 1)

# result = 0
# for tar in range(1 << n):
#     # 두 명 이상인 경우만
#     if get_count(tar) >= 2:
#         result += 1
# print(result)

# run(0, 0)