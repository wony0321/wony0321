import sys
sys.stdin = open('4880_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))

    info = {'scissors': 1, 'rock': 2, 'paper': 3}
    print(num_lst)