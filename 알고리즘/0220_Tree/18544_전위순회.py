import sys
sys.stdin = open('18544_input.txt')

# 전위순회 함수 만들기
def pre_order(T):
    if T:   # 없는 정점이 0이니까 T가 0이 아니면?
        print(T, end = ' ')
        pre_order(left[T])
        pre_order(right[T])

# 정점의 총 수
V = int(input())
# 정점의 번호
N = V-1
# V-1개의 간선 나열 리스트
edge_lst = list(map(int, input().split()))

# 왼쪽 자식 노드 넣을 리스트 만들기 (부모 노드 인덱스랑 맞춤)
left = [0] * (V+1)
# 오른쪽 자식 노드 넣을 리스트 만들기 (부모 노드 인덱스랑 맞춤)
right = [0] * (V+1)
# 자식을 인덱스로 한 부모 노드 리스트 만들기
par = [0] * (V+1)

for i in range(N):
    # 간선 리스트에서 부모와 자식 노드 설정
    p, c = edge_lst[i*2], edge_lst[i*2+1]
    # 부모 노드의 번호를 left에서 확인해봤을 때
    if not left[p]:
        left[p] = c
    else:
        right[p] = c
    # 자식 인덱스를 부모 노드에 저장
    par[c] = p

# 마지막 정점을 넣어줌
c = N
# 값이 0이면 부모가 없다는 의미, 0이 아니면 부모가 존재
while par[c] != 0:
    c = par[c]
root = c
pre_order(root)