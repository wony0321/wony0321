import sys
sys.stdin = open('5177_input.txt')

def enq(n):
    global last
    last += 1
    h[last] = n
    c = last
    p = c//2
    while p >= 1 and h[p] > h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c//2

# def deq():
#     global last
#     tmp = h[1]
#     h[1] = h[last]
#     last -=


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    h = [0]*(N+1)
    last = 0
    for num in arr:
        enq(num)

    ans_idx = N//2
    ans = 0
    while ans_idx >= 1:
        ans += h[ans_idx]
        ans_idx = ans_idx//2

    print(f'#{tc} {ans}')