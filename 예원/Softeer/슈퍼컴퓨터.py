import sys

sys.stdin = open('6252_input.txt')

# 성능이 가장 낮은 컴퓨터의 성능 최대화
# 한 컴퓨터에 2번 이상 업드레이드 수행 불가
# 성능을 d만큼 향상시키는 데에 드는 비용은 d^2


T = int(input())
for tc in range(1, T + 1):
    # N대의 컴퓨터, B원의 예산
    N, B = map(int, input().split())
    # 컴퓨터의 성능 리스트
    arr = list(map(int, input().split()))
    arr.sort()

    def test(x):
        # 비용을 0으로 초기화
        cost = 0
        for i in range(N):
            if arr[i] < x:
                cost += (x-arr[i])**2
        if cost <= B:
            return True
        else:
            return False

    # 이진 탐색 사용
    low, high = 1, 2*10**9

    while low < high:
        # high = low+1인 경우에는 무한 루프에 빠짐 (low+low+1)//2 = low
        mid = (low + high + 1) // 2
        if test(mid):
            low = mid
        else:
            high = mid-1

    print(low)