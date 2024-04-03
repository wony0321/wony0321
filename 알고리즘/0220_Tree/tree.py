'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(T):
    if T:   # 없는 정점이 0이니까 0이 아니면 T
        print(T, end = ' ')
        pre_order(left[T])
        pre_order(right[T])


N = int(input())        # 1번부터 N번까지인 정점
E = N-1
arr = list(map(int, input().split()))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장
right = [0]*(N+1)
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
# for i in range(0, N*2, 2):
#     p, c = arr[i], arr[i+1]
    if left[p] == 0:      # 왼쪽 자식이 없으면
        left[p] = c
    else:               # 오른쪽 자식이 없으면
        right[p] = c
    par[c] = p

# 루트 찾는 방법
c = N   # 마지막 정점 넣기
while par[c] != 0:      # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root
print(root)
print('------')
pre_order(root)