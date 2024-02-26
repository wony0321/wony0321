import sys
sys.stdin = open('18311_input.txt')

def dfs(i, E):
    visited = [0] * E
    stack = []
    visited[i] = 1
    print(i, end='')
    while True:
        for w in adjl[i]:
            if visited[w] == 0:
                stack.append(i)
                i = w
                visited[i] = 1
                print('-', w, sep='', end='')
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break

T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    adjl = [[] for _ in range(E)]

    for i in range(V):
        n1, n2 = arr[i*2], arr[i*2+1]
        adjl[n1].append(n2)
        adjl[n2].append(n1)

    print(f'#{tc}', end=' ')
    dfs(1, E)