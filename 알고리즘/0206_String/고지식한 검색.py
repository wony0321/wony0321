def f(pat, txt, M, N):
    for i in range(N-M+1):  # text에서 비교 시작 위치
        for j in range(M):
            if txt[i+j] != pat[j]:  # 불일치면 다음 시작위치로 감
                break
        # for문이 정상적으로 끝난 경우는 for문 나오게 되므로, 여기서 바로 아래와 같이 써도됨
        else:  # for문이 잘 끝났으면! 이거로!! 패턴매칭에 성공하면 1 반환
            return 1
        # 모든 위치에서 비교가 끝난 경우
        return 0

T = int(input())
for tc in range(1, T+1):
    pat = input()
    txt = input()
    M = len(pat)
    N = len(txt)

    ans = f(pat, txt, M, N)
    print(f'#{tc} {ans}')