import sys
sys.stdin = open('9367_input.txt')

T = int(input())
for tc in range(1, T+1):
    # 당근의 개수
    N = int(input())
    # 당근의 크기
    C = list(map(int, input().split()))

