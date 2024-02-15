arr = [1, 5, 7, 3, 2, 0, 6, 44, 22]

def select(arr, k):
    for i in range(0, k):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[k-1]

print(select(arr, 4))