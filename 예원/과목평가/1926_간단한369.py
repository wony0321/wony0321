import sys
sys.stdin = open('1926_input.txt')

N = int(input())

num_lst = [str(i) for i in range(1, N+1)]

for i in range(N):
    cnt = 0
    for n in num_lst[i]:
        if int(n) != 0 and int(n) % 3 == 0:
            num = ''
            cnt += 1
    if cnt > 0:
        num_lst[i] = '-'*cnt

print(*num_lst)
