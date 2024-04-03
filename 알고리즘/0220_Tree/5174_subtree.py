import sys
sys.stdin = open('5174_input.txt')

def pre_order(T):
    global cnt
    if T:
        cnt += 1
        pre_order(left[T])
        pre_order(right[T])

T = int(input())
for tc in range(1, T+1):
    # E: 간선의 개수, N: 찾고자 하는 루트
    E, N = map(int, input().split())

    V = E+1
    # 왼쪽 자식 노드 넣을 리스트 만들기 (부모 노드 인덱스랑 맞춤)
    left = [0] * (V + 1)
    # 오른쪽 자식 노드 넣을 리스트 만들기 (부모 노드 인덱스랑 맞춤)
    right = [0] * (V + 1)
    # 자식을 인덱스로 한 부모 노드 리스트 만들기
    par = [0] * (V + 1)
    # 노드 세기
    cnt = 0

    edge_lst = list(map(int, input().split()))

    for i in range(E):
        p, c = edge_lst[i*2], edge_lst[i*2+1]

        if not left[p]:
            left[p] = c
        else:
            right[p] = c
        par[c] = p

    pre_order(N)
    print(f'#{tc} {cnt}')