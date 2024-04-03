import sys
sys.stdin = open('1231_input.txt')

def in_order(T):
    # 없는 정점이 0이니까 T가 0이 아니면?
    global ans
    if T:
        in_order(left[T])
        # ans.append(str_lst[T])
        ans += str_lst[T]
        in_order(right[T])


T = 10
for tc in range(1, T+1):
    # 정점의 총 수
    N = int(input())
    # 정점들의 인덱스 번호
    V = N-1
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    str_lst = [0] * (N + 1)
    par = [0] * (N + 1)
    # ans = []
    ans = ''
    for _ in range(N):
        info = list(map(str, input().split()))
        v_num = int(info[0])
        v_str = info[1]
        str_lst[v_num] = v_str

        if len(info) == 3:
            left[v_num] = int(info[2])
            par[int(info[2])] = v_num
        elif len(info) == 4:
            left[v_num] = int(info[2])
            right[v_num] = int(info[3])
            par[int(info[2])] = v_num
            par[int(info[3])] = v_num

    c = V
    while par[c] != 0:
        c = par[c]
    root = c
    in_order(root)
    print(f'#{tc} {ans}')





