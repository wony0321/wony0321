import sys
sys.stdin = open('18795_input.txt')

# 방법 1
def quickSort1(target):
    N = len(target)
    if N <= 1:
        return target

    middle_num = target[N//2]
    left, middle, right = [], [], []

    for num in target:
        if num == middle_num:
            middle.append(num)
        elif num < middle_num:
            left.append(num)
        else:
            right.append(num)
    return quickSort1(left) + middle + quickSort1(right)

# 방법 2
def quickSort2(arr):
    def sort(left, right):
        if left >= right:
            return
        middle = partition(left, right)
        sort(left, middle-1)
        sort(middle, right)

    def partition(left, right):
        pivot = arr[(left+right)//2]
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1
        return left
    return sort(0, len(arr)-1)

# 방법 3
def s(left, right):
    if left >= right:
        return
    middle = par(left, right)
    s(left, middle-1)
    s(middle, right)

def par(left, right):
    pivot = arr[(left+right)//2]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
    return left


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    # 방법 1 출력
    ans = quickSort1(arr)
    print(f'#{tc}', *ans)

    # 방법 2 출력
    # quickSort2(arr)
    # print(arr)

    # 방법 3 출력
    # s(0, len(arr)-1)
    # print(arr)

