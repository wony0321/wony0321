import sys
sys.stdin = open('4831_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    m_lst = list(map(int, input().split())) # M개의 정류장 번호

    counts = [0] * N

    for x in m_lst:
        counts[x] += 3



