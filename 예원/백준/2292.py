N = int(input())

cnt = 1
grow = 1
while N > grow:
    grow += cnt * 6
    cnt += 1
print(cnt)