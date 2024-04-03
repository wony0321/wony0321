arr = [3, 4, 6, 8, 22, 1, 5, 6, 33, 66]
print(arr)
N = len(arr)

def selectionSort(a, N):
    # 구간의 시작 i
    for i in range(N-1):    # 주어진 구간의 시작 i, 2개의 원소가 남을 때까지
        min_idx = i         # 맨 앞 원소를 최솟값 위치(min_idx)로 가정
        for j in range(i+1, N):     # 실제 최솟값 찾을 위치 j 검색
            if a[min_idx] > a[j]:       # 여기서 괜히 if문 더 넣어서 늘리지 말자
                min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
    return
selectionSort(arr, N)
print(arr)