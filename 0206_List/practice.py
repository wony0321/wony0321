p ="is"
t = "This is a book~!"
M = len(p)
N = len(t)

# def BruteForce(p, t):
#     i = 0
#     j = 0
#     while j < M and i < N:
#         if t[i] != p[j]:
#             i = i - j
#             j = -1
#             # else로 쓸거면, i = i - j - 1, j = 0으로 가능
#             # 이중 for문도 가능
#         i = i + 1
#         j = j + 1
#     if j == M:
#         return i - M
#     else:
#         return -1

result = t.find(p)
print(result)