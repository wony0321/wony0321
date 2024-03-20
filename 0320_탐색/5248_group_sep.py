import sys
sys.stdin = open('5248_input.txt')

# 전체 몇개의 조가 만들어지는지를 출력해야 함

T = int(input())
for tc in range(1, T+1):
    # N번까지의 학생, M장의 신청서
    N, M = map(int, input().split())
    M_arr = list(map(int, input().split()))

