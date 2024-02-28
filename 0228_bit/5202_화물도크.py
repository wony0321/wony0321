import sys
sys.stdin = open('5202_input.txt')

T = int(input())
for tc in range(1, T+1):
    # N: 신청서 개수
    N = int(input())
    reserve = []
    for _ in range(N):
        s, e = map(int, input().split())
        reserve.append((s, e))

    # 신청서 종료 시간 기준으로 오름차순 정렬하기
    reserve.sort(key=lambda x: (x[1], x[0]), reverse=False)
    cnt = 1
    turn = reserve[0][1]

    for idx in range(1, len(reserve)):
        if turn <= reserve[idx][0]:
            turn = reserve[idx][1]
            cnt += 1
    print(f'#{tc} {cnt}')