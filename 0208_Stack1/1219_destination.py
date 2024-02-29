# 인접리스트저장이나 배열 저장으로 하면 풀릴 것
# 모든 길은 일방통행

import sys
sys.stdin = open('1219_input.txt')

def dfs(start, end):
    visited = [0] * (end+1)
    stack = []
    visited[start] = 1
    while True:
        for w in adjl[start]:
            if w == 99:
                return 1
            # 방문이 가능한지 확인
            if visited[w] == 0:
                # 되돌아오기 위해서 stack에 값 넣어주기
                stack.append(start)
                start = w
                visited[start] = 1
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break
    return 0


T = 10
for _ in range(T):
    tc, road = map(int, input().split())
    arr = list(map(int, input().split()))
    # 인접 리스트 만들기
    adjl = [[] for _ in range(road+1)]

    start = 0
    end = 99

    for i in range(road):
        n1, n2 = arr[i*2], arr[i*2+1]
        adjl[n1].append(n2)

    print(f'#{tc} {dfs(start, end)}')