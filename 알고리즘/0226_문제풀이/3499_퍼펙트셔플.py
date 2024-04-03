import sys
sys.stdin = open('3499_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(str, input().split()))

    a = 0
    b = (N+1)//2

    print(f'#{tc}', end=' ')
    for turn in range(N):
        if turn % 2 == 0:
            print(card[a], end=' ')
            a += 1
        else:
            print(card[b], end=' ')
            b += 1
    print()
