# # N: 손님의 수
# # 각 손님마다 도착 시간
# # M: K개 만드는 데 걸리는 시간, K: M초에 만들 수 있는 빵 수
#
# N = 4
# M = 3
# K = 2
# arr = [3, 4, 6, 9]
#

# cnt = 0
# for n in range(N):
#     if n+1 <= (arr[n]/M)*K:
#         cnt += 1
# if cnt == N:
#     print('Possible')
# else:
#     print('Impossible')
#
# def start():
#     sold_bread = 0
#     # 공식, 특정 시간에 만들 수 있는 빵의 개수
#     for person in customers:
#         made_bread = (person // m) * k
#
#         # 빵을 1개 팔았다
#         sold_bread += 1
#
#         # 재고 계산
#         remain = made_bread - sold_bread
#
#         # 재고가 0보다 작으면 실패
#         if remain < 0:
#             return 'Impossible'
#     # 실패가 없었으면 성공
#     return 'Possible'
#
# T = int(input())
# for tc in range(1, T+1):
#     # 손님수 n, m초에 k개의 빵을 만든다. 손님들이 도착하는 시간 customers
#     n, m, k = map(int, input().split())
#     customers = list(map(int, input().split()))
#
#     customers.sort() # 오름차순 sort
#     result = start()
#     print(f'#{tc} {result}')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))

    customers.sort()

    cnt = 0
    for n in range(N):
        made_bread = (customers[n] // M) * K
        if made_bread - (n + 1) >= 0:
            cnt += 1
    if cnt == N:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')