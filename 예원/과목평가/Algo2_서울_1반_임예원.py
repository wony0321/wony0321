import sys
sys.stdin = open('algo2_sample')

# 행렬 탐색
# 최대값의 합을 구하는 놀이
# N*N 크기 행렬에서 M*M 크리 행렬 탐색
# M*M에서의 최댓값을 다시 시작점으로 하여 탐색
# 시작점이 행렬내 최댓값이면 행렬 탐색 종료
# 범위 벗어나면 A 범위 내에서만 탐색


T = int(input())
for tc in range(1, T+1):
    # N: 전체 행렬 크기, M: 탐색할 행렬 크기
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    start_i = 0
    start_j = 0
    max_sum = [0]
    max_i = 0
    max_j = 0

    while True:
        max_num = max_sum[-1]
        for i in range(start_i, start_i+M):
            for j in range(start_j, start_j+M):
                if 0 <= i < N and 0 <= j < N:
                    if max_num < arr[i][j]:
                        max_num = arr[i][j]
                        max_i = i
                        max_j = j
        # max_num이 더이상 안바뀌면,,, 어떻게 표현해야 하나ㅠ
        if max_sum[-1] == max_num:
            break
        # 여기 append 하는 위치 주의!
        max_sum.append(max_num)
        start_i = max_i
        start_j = max_j

    print(f'#{tc} {sum(max_sum)}')