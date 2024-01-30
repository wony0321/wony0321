import sys
sys.stdin = open('flatten_input.txt')

# 정렬
def sorting(lst, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

T = 10

for test_case in range(1, T+1):
    dump = int(input())
    arr = list(map(int, input().split()))

# arr 리스트에 주어진 숫자들 중에서 가장 큰 값과 가장 작은 값을 구함
# 덤프를 다 돌리고 나서 최고점과 최저점의 높이 차 반환
# 가장 큰 값에서 -1, 가장 작은 값에서 +1
    # 이걸 for문 돌리되, 덤프 횟수 제한 (주어진 수)
    # 덤프 횟수 이내에 평탄화 완료되면 그냥 반환

    for d in range(dump):
        sorting(arr, 100)
        arr[-1] -= 1
        arr[0] += 1

    sorting(arr, 100)

    print(f'#{test_case} {arr[99] - arr[0]}')