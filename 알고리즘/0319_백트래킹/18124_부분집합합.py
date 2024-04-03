import sys
sys.stdin = open('18124_input.txt')

def dfs(i):
    global ans
    if ans:
        return
    if i == 10:
        if len(visited) != 0 and sum(visited) == 0:
            ans = 1
        return

    visited.append(arr[i])
    dfs(i+1)
    visited.pop()
    dfs(i+1)

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    visited = []
    ans = 0
    dfs(0)
    print(f'#{tc} {ans}')