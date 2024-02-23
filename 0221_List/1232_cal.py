import sys
sys.stdin = open('1232_input.txt')

cal = ['+', '-', '*', '/']

T = 10
for tc in range(1, T+1):
    # 정점의 개수
    N = int(input())
    # N 줄에 걸친 정점 정보
    node_info = [list(map(str, input().split())) for _ in range(N)]

    h = [0] * (N+1)
    last = N

    ans = 0

    for i in range(N-1, -1, -1):
        if node_info[i][1].isnumeric():
            h[i+1] = int(node_info[i][1])
        else:
            h[i+1] = node_info[i][1]
            if node_info[i][1] == cal[0]:
                ans = int(node_info[i][2]) + int(node_info[i][3])
            elif node_info[i][1] == cal[1]:
                ans = int(node_info[i][2]) - int(node_info[i][3])
            elif node_info[i][1] == cal[2]:
                ans = int(node_info[i][2]) * int(node_info[i][3])
            elif node_info[i][1] == cal[3]:
                ans = int(node_info[i][2]) // int(node_info[i][3])

    print(ans)

    # ans = 0
    # while last > 1:
    #     for i in range(N-1, -1, -1):
    #         if not h[i].isnumeric():
    #             if h[i] == cal[0]:
    #                 ans = int(h[i*2]) + int(h[i*2+1])
    #             elif h[i] == cal[1]:
    #                 ans = float(h[i*2]) - float(h[i*2+1])
    #             elif h[i] == cal[2]:
    #                 ans = int(h[i*2]) * int(h[i*2+1])
    #             elif h[i] == cal[3]:
    #                 ans = int(h[i*2]) // int(h[i*2+1])
    #         last -= 1
    #
    # print(ans)