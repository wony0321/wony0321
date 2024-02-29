import sys
sys.stdin = open('4875_input.txt')

# 시작 위치를 찾는 함수
def find_start():
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                return r, c

def find_path(row, col):
    global result
    if result:  # result가 1이라면(이미 도착) 더이상 델타 탐색 안하도록
        return
    for i in range(4):      # 델타 탐색을 위한 반복
        nr = row + dr[i]
        nc = col + dc[i]
        # 이동할 좌표가 미로 범위 내인지 확인, 벽이 아닌 경우(이동 가능)
        if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1':
            if maze[nr][nc] == '3':
                result = 1
                return
            elif maze[nr][nc] == '0':
                # 이동할 위치를 방문 처리
                maze[nr][nc] = '1'      # 다시 탐색할 수 없도록 '1'로 변경(visited 대신)
                find_path(nr, nc)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    # 델타 탐색을 위한 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 시작 위치를 찾아야 됨
    r, c = find_start()
    result = 0
    find_path(r, c)
    print(f'#{tc} {result}')