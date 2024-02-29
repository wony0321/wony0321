def f(i, k):
    if i == k:
        print('end')
    else:
        f(i+1, k)

f(0, 1000)