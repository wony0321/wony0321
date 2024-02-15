import sys
sys.stdin = open('4875_input.txt')

# 강사님 풀이
class Stack:
    def __init__(self, size):
        self.top = -1
        self.stack = [0]*size
        # 여기서 self는 인스턴스 변수

    # stack의 가장 위에 있는 값 추출 매서드
    def peek(self):
        return self.stack[self.top]

    def is_full(self):
        # top이 마지막 인덱스에 위치해 있는지 비교
        return self.top == len(self.stack) - 1

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        if self.is_full():
            print('Full~~~~~~')
            return 0
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            print('Empty~~~~~')
            return 0
        else:
            value = self.peek()
            self.stack[self.top] = 0
            self.top -= 1
            return value

# 시작 위치를 찾는 함수
def find_start():
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                return r, c

# 목적이 출구에 도착할 수 있는지 여부이기 때문에 backtracking 사용
# DFS는 모든 정점에 방문하는 것이 목표임
def find_path(r, c):
    result = 0 # 도착 여부 저장
    # 시작 위치부터 델타 탐색을 해야 함
    stack = Stack(N*N)
    stack.push((r, c))
    row, col = r, c
    # stack이 비어있다 = 더이상 이동할 수 잇는 곳이 없다
    # so stack이 비어있지 않은 이상 계속해서 돌겠다
    # result가 0은 도착하지 않은 경우를 말함
    while not stack.is_empty():
        # 델타 탐색
        for i in range(4):      # 델타 탐색을 위한 반복
            nr = row + dr[i]
            nc = col + dc[i]
            # 이동할 좌표가 미로 범위 내인지 확인, 벽이 아닌 경우(이동 가능)
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1':
                if maze[nr][nc] == '3':
                    return 1
                elif maze[nr][nc] == '0':
                    # 이동할 위치를 방문 처리
                    maze[nr][nc] = '1'      # 다시 탐색할 수 없도록 '1'로 변경(visited 대신)
                    # 돌아올 위치(좌표)를 stack에 저장
                    stack.push((row, col))
                    # 이동
                    row, col = nr, nc
                    break       # 찾으면 그냥 초기화하고 다시 상하좌우 탐색 위해 break
        else:
        # 더 이상 갈 곳이 없다면 stack에서 pop해서 탐색을 이어서 진행
            if not stack.is_empty():
                row, col = stack.pop()      # 다시 되돌아가서 델타 탐색 진행
    return 0    # 도착할 수 없음을 의미(while에서 stack이 비어있으면 이동할 곳도 없기 때문)
                # return 1을 못만나고 여기까지와버림

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]


    '''
    # 미로의 통로와 벽에 대한 정보를 딕셔너리로 만들기
    way = {'cor': '0', 'wall': '1', 'start': '2', 'des': '3'}

    di = [0, -1, 0, 1]  # 오, 위, 왼, 아래
    dj = [1, 0, -1, 0]  # 오, 위, 왼, 아래

    # 도착할 수 있으면 1, 없으면 0 출력

    start = 0
    des = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start = [i, j]
            elif arr[i][j] == '3':
                des = [i, j]

    while start != des:
        for k in range(4):
            ni = start[0] + di[k]
            nj = start[1] + dj[k]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == '0':
                # start.clear()
                start = [ni, nj]
            else:
    print(start)
    '''

    # 강사님 풀이
    # 재귀, stack 써서 돌아올 경로 저장
    # 가지치기
    # DFS 코드와 유사하게 작성될 것
    # 델타 탐색을 하고 막혔을 때 되돌아오는 stack 적용

    # 델타 탐색을 위한 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 시작 위치를 찾아야 됨
    r, c = find_start()
    result = find_path(r, c)

    print(f'#{tc} {result}')