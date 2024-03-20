import sys
sys.stdin = open('5207_input.txt')

def binary_search(target, start, end, direction):
    global count
    # direction: 이전에서 탐색 위치(1. 왼 / 2. 오)
    # 종료 조건
    if start > end:
        return -1

    mid = (start+end) // 2
    middle = A[mid]
    # 가운데 있는 값이 찾으려는 값이면 종료
    if target == middle:
        count += 1
        return mid
    # 크면 오른쪽
    elif target > middle:
        if direction == 2:
            return -1
        res = binary_search(target, mid+1, end, 2)
    # 작으면 왼쪽
    else:
        if direction == 1:
            return -1
        res = binary_search(target, start, mid-1, 1)
    return res

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 이진 탐색을 위해 A 정렬
    A.sort()
    count = 0  # 탐색 성공된 경우를 카운트
    # print(A, B)
    # B에 있는 값을 하나씩 A에 있는지 찾아야 함
    for t in B:
        # print(t, end=' > ')
        result = binary_search(t, 0, N-1, 0) # 시작은 왼쪽도 아니고 오른쪽도 아님
        # print(result, count)
    print(f'#{tc} {count}')