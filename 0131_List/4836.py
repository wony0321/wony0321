import sys
sys.stdin = open('4836_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N은 칠할 영역의 개수임
    color_lst = []
    for color in range(1, N+1):
        c = list(map(int, input().split()))
        color_lst.append(color)
    # print(color_lst)
    # [[2, 2, 4, 4, 1], [3, 3, 6, 6, 2]]
    # [[1, 2, 3, 3, 1], [3, 6, 6, 8, 1], [2, 3, 5, 6, 2]]
    # [[1, 4, 8, 5, 1], [1, 8, 3, 9, 1], [3, 2, 5, 8, 2]]

    for colors in color_lst:
        first = [colors[0], colors[1]]
        last = [colors[2], colors[3]]
        color = colors[-1]
        for i in range(first[0], first[1]+1):
            for j in range(last[0], last[1]+1):


