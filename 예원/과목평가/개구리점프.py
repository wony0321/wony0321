import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    # N = 연잎의 개수, K = 점프 횟수
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    try_num = 0  # 시도 횟수 저장
    point = 0  # 연잎에 적힌 숫자 합계 저장
    frog = arr[0]  # 개구리의 인덱스 번호 저장
    minus = 0  # 마이너스일때 값 저장시켜서 다음 번에는 더 뛰게

    while try_num < K:
        try_num += 1
        if frog > N-1 or frog < 0 or arr[frog] == 0:
            break

        if arr[frog] > 0:
            point += arr[frog]
            if minus != 0:
                frog += (abs(minus) + arr[frog])
            else:
                frog += arr[frog]
            minus = 0
        elif arr[frog] < 0:
            point += arr[frog]
            minus = arr[frog]
            frog += arr[frog]

    print(f'#{tc} {point}')