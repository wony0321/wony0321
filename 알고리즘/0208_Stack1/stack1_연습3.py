'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(i, V): # 정점 번호: i(시작), 마지막: V
    # visited, stack 생성 및 초기화
    visited = [0]*(V+1)
    stack = []
    visited[i] = 1  # 시작점 방문한 상황
    print(i)        # 정점에서 할 일
    while True: # 탐색하는 과정
        # 조건1: 현재 방문한 정점에 인접하고 방문 안한 정점 w가 있으면
        for w in adjl[i]:
            if visited[w] == 0:
                stack.append(i)     # push(i), i를 지나서
                i = w               # w에 방문
                visited[i] = 1      # 방문해서 할 일
                print(i)
                break   # for w를 break하는 것
            else:                   # i에 남은 인접 정점이 없으면, for w에 대한 else
                # 스택이 비어있지 않으면(지나온 정점이 남아 있으면)
                # 거기서부터 다시 시작하면 돼
                if stack:
                    i = stack.pop()
                else:
                    break   # while True, while문을 break하는 것
    # return #이건 생략 가능

V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)]  #adjl[i] 행에 i에 인접인 정점번호
for i in range(E):
    # 노드1, 노드2
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)  # 방향이 없는 경우 이 부분 써야 함

# print(adjl) # [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]

dfs(1, V)