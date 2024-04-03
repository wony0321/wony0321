import sys
sys.stdin = open('10580_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    lst = []
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        lst.append((Ai, Bi))

    # 첫 번째 원소를 기준으로 오름차순 정렬
    lst.sort(key = lambda x : x[0])
    cnt = 0
    for i in range(N):
        for tar in range(i):
            if lst[i][1] < lst[tar][1]:
                cnt += 1

    print(f'#{tc} {cnt}')