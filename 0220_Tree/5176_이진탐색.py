import sys
sys.stdin = open('5176_input.txt')

def in_order(T):
    # 없는 정점이 0이니까 T가 0이 아니면?
    global ans
    if T:
        in_order(left[T])
        lst.append(T)
        in_order(right[T])

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # N: 해당 노드 번호, N//2: 부모 노드 번호

    v_arr = []
    for i in range(2, N+1):
        v_arr.append(i//2)
        v_arr.append(i)
    # print(v_arr)

    left = [0] * (N+1)
    right = [0] * (N+1)
    par = [0] * (N+1)

    for i in range(N-1):
        p, c = v_arr[i*2], v_arr[i*2+1]
        if not left[p]:
            left[p] = c
        else:
            right[p] = c
        par[c] = p

    c = N
    while par[c] != 0:
        c = par[c]
    root = c
    lst = []
    in_order(root)
    print(f'#{tc} {lst.index(1)+1} {lst.index(N//2)+1}')

