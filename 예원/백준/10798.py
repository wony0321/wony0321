# import sys
# sys.stdin = open('10798_input.txt')
#
# T = int(input())
# for tc in range(1, T+1):
# word_lst = [list(map(str, input().strip())) for _ in range(5)]
# word_check = ['' for _ in range(16)]
#
# for i in range(5):
#     for j in range(len(word_lst[i])):
#         word_check[j] += word_lst[i][j]
#
# for w in range(16):
#     print(word_check[w], end='')

# N: 수, B: 진법
N, B = map(str, input().split())
alph_num = {chr(i+65) : i+10 for i in range(26)}

ans = 0

for i in range(len(N)-1, -1, -1):
    if N[i].isnumeric():
        ans += int(N[i])*(int(B)**(len(N)-i))
    else:
        ans += alph_num[N[i]]*(int(B)**i)

print(ans)