import sys
sys.stdin = open('5248_input.txt')

def find_set(x):
    # 자기 자신이 부모면 그걸 뽑고
    if parents[x] == x:
        return x
    # 아니라면 다시 돌리면서 부모 찾자!
    return find_set(parents[x])

def union_set(x, y):
    x = find_set(x)
    y = find_set(y)

    # 같으면 그걸 돌려내고
    if x == y:
        return

    # 같지 않으면 합쳐라
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 전체 몇개의 조가 만들어지는지를 출력해야 함

T = int(input())
for tc in range(1, T+1):
    # N번까지의 학생, M장의 신청서
    N, M = map(int, input().split())
    M_arr = list(map(int, input().split()))

    parents = [i for i in range(N+1)]

    for n in range(M):
        union_set(M_arr[n*2], M_arr[n*2+1])

    for i in range(N+1):
        parents[i] = find_set(i)

    # print(parents)
    par_set = set(parents[1:])
    print(f'#{tc} {len(par_set)}')