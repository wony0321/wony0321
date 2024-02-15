import sys
sys.stdin = open('4831_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # K: 최대한 이동할 수 있는 정류장 수, N: 종점 번호, M: 충전기가 설치된 정류장 개수
    m_lst = list(map(int, input().split())) # M개의 정류장 번호

    # 정류장별로 초기값 설정
    counts = [0] * N
    # 충전기가 설치된 정류장에 +K
    for num in m_lst:
        counts[num] = K

    station = 0
    charge = 3

    for _ in range(N):
        charge -= 1
        if charge < 1:




