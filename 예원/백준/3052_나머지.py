# check = set()
# for _ in range(10):
#     N = int(input())
#     check.add(N % 42)
# print(len(check))

# S = input()
# i = int(input())
# print(S[i-1])

# T = int(input())
# for _ in range(T):
#     S = input()
#     print(S[0], S[-1], sep='')

# List =[chr(i) for i in range(0, 44)]
# print(List)
# S = list(input())
# for alph in aList:
#     if alph in S:
#         print(S.index(alph), end=' ')
#     else:
#         print(-1, end=' ')

# N = int(input())
# nums = list(map(int, input()))
# print(sum(nums))

# T = int(input())
# for _ in range(T):
#     P = ''
#     R, S = map(str, input().split())
#     for s in S:
#         P += s*int(R)
#     print(P)

# print(len(list(map(str, input().strip().split()))))

# A, B = map(str, input().split())
# print(max(int(A[::-1]), int(B[::-1])))

# aList =[[], [], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z'], ['OPERATOR']]
# word = input()
# word_idx = []
# time = 1
# temp_w = 0
# for w in word:
#     for i in range(len(aList)):
#         if w in aList[i]:
#             word_idx.append(i+1)
# word_idx.sort()
#
# print(sum(word_idx))

#
# print('         ,r\'\"7')
# print('r`-_   ,\'  ,/')
# print(' \\. \". L_r\'')
# print('   `~\\/')
# print('      |')
# print('      |')

# 체스판 킹1개, 퀸 1개, 룩2개, 비숍 2개, 나이트 2개, 폰 8개
# 입력값은 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰 개수 주어짐
# 0 1 2 2 2 7
white = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
for i in range(len(chess)):
    print(chess[i]-white[i], end=' ')
