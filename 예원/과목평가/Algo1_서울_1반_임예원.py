import sys
sys.stdin = open('algo1_sample_in.txt')

# 사격 게임
# 보너스 게임에서는 한발의 총 쏠 수 있음
# 쏜 칸에서 위, 아래, 좌, 우 2 칸씩 점수 합산
# 보너스 점수의 최댓값 구하기

T = int(input())
for tc in range(1, T+1):
    # 과녁 크기 (N*N)
    N = int(input())
    # 과녁 점수 판
    dart = [list(map(int, input().split())) for _ in range(N)]

    # 델타 탐색 이용 (우, 하, 좌, 상)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_score = 0

    for i in range(N):
        for j in range(N):
            score = dart[i][j]
            for k in range(4):
                # 각 방향에서 2칸씩 가야하므로 다시 for문 써서 값 출력
                for n in range(1, 3):
                    ni = i + di[k]*n
                    nj = j + dj[k]*n
                    if 0<=ni<N and 0<=nj<N:
                        score += dart[ni][nj]
            if max_score < score:
                max_score = score

    print(f'#{tc} {max_score}')