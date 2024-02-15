import sys
sys.stdin = open('4843_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    def selectionSort(arr, N):
        # 구간의 시작 i
        for i in range(N-1):  # 주어진 구간의 시작 i, 2개의 원소가 남을 때까지
            # 10번만 돌리기 위해,,어떻게해야하지?
            idx = i  # 맨 앞 원소를 비교 숫자로 가정
            for j in range(i+1, N):  # 실제 최솟값 찾을 위치 j 검색
                if i % 2 == 0:  # 0이랑 짝수 i 때는 최댓값을 구해서 넣음
                    if arr[idx] < arr[j]:
                        idx = j
                elif i % 2 != 0:           # 홀수 i 때는 최솟값을 구해서 넣음
                    if arr[idx] > arr[j]:
                        idx = j
            arr[i], arr[idx] = arr[idx], arr[i]
            # for문 밖에서 돌려야 함
        return

    selectionSort(arr, N)
    print(f'#{tc}', *arr[0:10])