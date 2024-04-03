import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    N_lst = []
    num = 0

    for i in range(N):
        new_lst = []
        for j in range(N):
            num += 1
            new_lst.append(num)
        N_lst.append(new_lst)
    print(N_lst)

    # arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # arr2 = [[0]*N for _ in range(N)]
    # print(arr2)

    # di = [0, 1, 0, -1]
    # dj = [1, 0, -1, 0]
    #
    # for i in range(N):
    #     for j in range(N):
    #