def quickSort(arr):
    N = len(arr)
    if N <= 1:
        return arr
    mid_num = arr[N//2]
    left, middle, right = [], [], []

    for num in arr:
        if num == mid_num:
            middle.append(num)
        elif num < mid_num:
            left.append(num)
        else:
            right.append(num)
    return quickSort(left) + middle + quickSort(right)
