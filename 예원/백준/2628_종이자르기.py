w, h = map(int, input().split())

slice_num = int(input())

w_lst = [0, h]
h_lst = [0, w]
w_max = 0
h_max = 0

# 가로 0, 세로 1
for _ in range(slice_num):
    way, num = map(int, input().split())

    if way == 0:
        w_lst.append(num)
    else:
        h_lst.append(num)

w_lst.sort()
h_lst.sort()

i = 1
while i < len(w_lst):
    w_len = w_lst[i]-w_lst[i-1]
    if w_max < w_len:
        w_max = w_len
    i += 1
j = 1
while j < len(h_lst):
    h_len = h_lst[j]-h_lst[j-1]
    if h_max < h_len:
        h_max = h_len
    j += 1

print(w_max*h_max)