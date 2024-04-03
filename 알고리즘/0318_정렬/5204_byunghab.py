import sys
sys.stdin = open('5204_input.txt')

# mergesort 방법 1
def mergeSort(arr):
    global cnt
    if len(arr) <= 1:
        return arr

    middle = len(arr)//2
    left = mergeSort(arr[0:middle])
    right = mergeSort(arr[middle:])
    if left[-1] > right[-1]:
        cnt += 1

    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    return result

# mergesort 방법 2
def merge_sort(arr):
    global cnt
    if len(arr) < 2:
        return arr
    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    merged_arr = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1
    merged_arr += left[l:] + right[r:]

    if left[-1] > right[-1]:
        cnt += 1

    return merged_arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    # 방법 1 출력
    ans = mergeSort(arr)
    print(f'#{tc} {ans[N//2]} {cnt}')

    # 방법 2 출력
    ans = merge_sort(arr)
    print(f'#{tc} {ans[N//2]} {cnt}')
