import sys
sys.stdin = open('5247_input.txt')

cal = ['+1', '-1', '*2', '-10']

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
