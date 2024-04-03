import sys
sys.stdin = open('16910_input.txt')

def get_count(N):
    cnt = 0
    for y in range(-N, N+1):
        for x in range(-N, N+1):
            ans = x**2 + y**2
            if ans <= N**2:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # arr = []
    #
    # for i in range(-N, N+1):
    #     for j in range(-N, N+1):
    #         arr.append([i, j])
    #
    # cnt = 0
    # for i in range(len(arr)):
    #     if arr[i][0]**2 + arr[i][1]**2 <= N**2:
    #         cnt += 1

    result = get_count(N)

    print(f'#{tc} {result}')