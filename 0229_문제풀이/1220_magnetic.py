import sys
sys.stdin = open('1220_input.txt')

# 열검사 함수
def get_sero_cnt(col):
    cnt = 0
    # red 자성체를 체크하기 위한
    is_red = False
    for row in range(N):
        # 1. red 자성체 발견
        if arr[row][col] == 1:
            is_red = True
        # 2. 이전에 red 자성체를 발견했고, 현재 blue 자성체 발견 cnt +=1
        elif is_red and arr[row][col] == 2:
            cnt += 1
            is_red = False  # 갱신
    return cnt

T = 10
for tc in range(1, T+1):
    # 정사각형 테이블의 변 길이 (100)
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_cnt = 0

    # 1은 N극, 2는 S극
    for col in range(N):
        total_cnt += get_sero_cnt(col)
    print(f'#{tc} {total_cnt}')