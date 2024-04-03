import sys
sys.stdin = open('5205_input.txt')

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

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = quickSort1(arr)
    print(f'#{tc} {ans[N//2]}')