X = int(input())

cnt = 0
ans = (0, 0)

num = 1
max_num = 1

while cnt < X:
    max_num += num
    num += 1


if num % 2 == 0:
    ans = (cnt, X-cnt+1)
elif num % 2 != 0:
    ans = (X-cnt+1, cnt)

print(f'{ans[0]}/{ans[1]}')
