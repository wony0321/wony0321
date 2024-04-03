import sys
sys.stdin = open('5178_input.txt')

T = int(input())
for tc in range(1, T+1):
    # N: 노드의 개수, M: 리프 노드의 개수, L: 값을 출력할 노드 번호
    N, M, L= map(int, input().split())
    # 리프 노드 번호와 자연수
    node = [list(map(int, input().split())) for _ in range(M)]

    h = [0]*(N+1)
    last = M

    for i in range(M):
        h[node[i][0]] = node[i][1]

    while last > 1:

        if not N%2:
            if last == M:
                h[last] = h[last*2]
            else:
                h[last] = h[last * 2] + h[last * 2 + 1]
            last -= 1
        else:
            last -= 1
            h[last] = h[last*2] + h[last*2+1]

    print(f'#{tc} {h[L]}')