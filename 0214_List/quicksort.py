def quickSort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)    # 분할
        quickSort(a, begin, p-1)    # 작은 부분
        quickSort(a, p+1, end)      # 큰 부분

def partition(a, begin, end):
    pivot = (begin+end) // 2
    L = begin   # 왼쪽 index
    R = end     # 오른쪽 index
    while L < R:
        while L<R and a[L]<a[pivot]:    # 탐색 조건 & 현재 위치가 기준값보다 작다면
            L += 1                      # 현재 위치가 기준값보다 크다면 while문 종료될 것
        while L<R and a[R]>=a[pivot]:
            R -= 1
        if L < R:
            if L==pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]     # 큰 값과 작은 값을 교환
    a[pivot], a[R] = a[R], a[pivot]
    return R        # 최종 위치

a = [69, 10, 3, 2, 16, 8, 31, 22]
begin = 0
end = len(a)-1
quickSort(a, begin, end)
# quickSort(a, begin, end)
print(a)