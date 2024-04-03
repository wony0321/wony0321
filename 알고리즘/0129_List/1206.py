import sys
sys.stdin = open('1206_input.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input()) # 건물의 개수
    arr = list(map(int, input().split())) # 각 건물의 높이를 리스트로 반환
    # print(N)
    # print(arr)

    # 왼쪽으로 2칸, 오른쪽으로 2칸 떨어진 것 확인하기
    cnt = 0

    좌우 2칸 중 가장 높은 빌딩의 높이를 구하고 내 높이에서 그것을 빼면 조망권 확보된 층이 몇 층인지 알 수 있음
    모든 빌딩을 다 조사해야 함
        현재 빌딩을 기준으로 좌측 2개, 우측 2개의 빌딩 높이를 조사
        4개의 빌딩을 조사할 때, 가장 높은 빌딩을 찾아내면
        나보다 높은지 확인하고 낮으면 빼도 됨
        뺀 값을 하나의 변수에 누적해 놓고 반환하면 끝!
    제약 사항
        가로 최대 길이 1000
        세로 최대 길이 255
        맨 왼쪽, 맨 오른쪽 각 두 칸은 빌딩이 지어지지 않음(높이 0)

    for i in range(2, N-2): # 3번째 건물부터 확인해서, 마지막에서 세번째 건물까지 확인
        h_lst = []
        for j in range(i-2, i+3):
            if arr[i] > arr[j]: # 더 크다면 조망권 확보되는 것이므로
                h = arr[i] - arr[j] # 높이 차이
                h_lst.append(h)
            elif i == j:
                continue
            else:
                h_lst.append(0)

        for num1 in range(len(h_lst)-1, 0, -1):
            for num2 in range(0, num1):
                if h_lst[num2] > h_lst[num2 + 1]:
                    h_lst[num2], h_lst[num2 + 1] = h_lst[num2 + 1], h_lst[num2]

        if h_lst[0] > 0:
            cnt += h_lst[0]

T = 10
for tc in range(1, T+1):
    N = int(input())  # 총 건물의 개수
    building_lst = list(map(int, input().split()))
    result = 0 # 조망권 개수를 저장하는 변수
    # 모든 빌딩 리스트를 확인해야 함
    # 좌, 우 2칸 씩
    # 인덱스 접근 방식의 반복 -> 좌, 우 2칸씩 접근하려면 요소 반복 보다는 인덱스 반복이 유리
    #빌딩 리스트의 길이만큼 range를 이용하면 됨
    for idx in range(N):
        # building_lst[idx] : idx 현재위치로 현재 빌딩 높이에 접근 가능
        # 빌딩을 확인해야 하는데 높이가 0인 것은 확인할 필요 없음
        if building_lst[idx] != 0:
            delta_idx = [-2, -1, 1, 2] # 좌측 2, 좌측 1, 우측 1, 우측 2
            # idx + delta_idx[n] n번 인덱스의 위치의 빌딩 높이를 확인할 수 있음
            # building_list[idx + delta_idx[0]] : 좌측 2번째 빌딩의 높이를 알 수 있다.
            # building_list[idx + delta_idx[3]] : 우측 2번째 빌딩의 높이를 알 수 있다.
            # 가장 높은 건물 확인
            max_height = 0
            for n in range(4): # 4번 반복 (좌, 우 총 4개만 확인하면 되기 때문)
                if max_height < building_lst[idx + delta_idx[n]]:
                    max_height = building_lst[idx + delta_idx[n]]

            # 현재 빌딩의 높이와 가장 큰 빌딩의 높이를 비교
            # 그리고 조망권을 확보할 수 있는지 계산
            if building_lst[idx] > max_height:
                result += building_lst[idx] - max_height # 조망권을 누적

    # 누적된 result를 출력
    print(f'#{tc} {result}')