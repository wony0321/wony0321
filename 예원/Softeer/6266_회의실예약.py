import sys
sys.stdin = open('6266_input.txt')

# 회의실은 9시부터 18시까지만 사용 가능하다
# 회의의 시작 시각은 회의의 종료 시각을 1시간 이상 앞선다.


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    room_name = [list(map(str, input().split())) for _ in range(N)]
    print(room_name)
    # info = [list(map(str, input().split())) for _ in range(M)]
    time_lst = [[] for _ in range(N)]
    for _ in range(M):
        r, s, t = map(str, input().split())
        idx = room_name.index([r])
        time_lst[idx].append((int(s), int(t)))
    print(time_lst)