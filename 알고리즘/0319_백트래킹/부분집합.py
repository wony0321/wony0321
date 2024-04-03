import sys
sys.stdin = open('4837_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [i for i in range(1, 13)]
    check = []
    cnt = 0

    def subset(level):
        global cnt
        if level == 12:
            if len(check) == N and sum(check) == K:
                cnt += 1
            return
        check.append(arr[level])
        subset(level+1)
        check.pop()
        subset(level+1)

    subset(0)
    print(f'#{tc} {cnt}')