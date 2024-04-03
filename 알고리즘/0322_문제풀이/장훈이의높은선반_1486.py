import sys
sys.stdin = open('1486_input.txt')

def dfs(cnt, sum_height):
    # 기저조건
    # 1. 모든 점원이 탑을 쌓았다면 종료
        # 현재까지 쌓은 점원의 수
    if cnt == N:
        # 제일 높이가 낮은 탑이 정답
        return
    # 2. 키의 합이 B이상이면 종료
        # 현재까지 쌓은 탑의 높이
    if sum_height >= B:
        # 제일 높이가 낮은 탑이 정답
        # 최소 탑의 높이는 재귀호출함수들이 "동시에" 사용함 -> 전역변수로 사용
        ans = min(ans, sum_height)
        return

    # 재귀호출파트
    dfs(cnt)
    dfs(cnt+1)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)
    dfs(0, 0)
    print(f'#{tc} {abs(ans-B)}')