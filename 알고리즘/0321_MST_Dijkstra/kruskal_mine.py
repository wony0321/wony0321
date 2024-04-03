import sys
sys.stdin = open('input.txt', 'r')

# 1. 전체 그래프를 보고, 가중치가 제일 작은 간선부터 뽑자
    # -> 코드로 구현: 전체 간선 정보를 저장 + 가중치로 정렬

# 2. 방문 처리
    # -> 이 때, 싸이클이 발생하면 안된다!
    # -> 싸이클 여부를 어떻게 알까? union-find 알고리즘 활용

def find_set(x):
    if parents[x] == x:
        return x
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 같은 집합이면 pass
    if x == y:
        return

    if x > y:
        parents[y] = x
    else:
        parents[x] = y

V, E = map(int, input().split())
# 간선 정보들을 모두 저장할 것
edges = []
for _ in range(E):
    # 출발, 도착, 가중치
    s, e, w = map(int, input().split())
    edges.append([s, e, w])

# 가중치를 기준으로 정렬
edges.sort(key=lambda x:x[2])

# 대표자 배열(자기자신을 바라봄)
parents = [i for i in range(V)]

# MST 완성은 = 간선의 개수가 V-1일때
# 선택한 edges의 수 카운트
cnt = 0
# 가중치 합
sum_weight = 0

# 가중치 낮은 것부터 뽑혀 나올 것.
# 간선들을 모두 확인한다.
for s, e, w in edges:
    # print(s, e, w)
    # 싸이클이 발생하면 pass
        # -> union-find에서 이미 같은 집합에 속해 있다면(대표자가 같다면) pass
    if find_set(s) == find_set(e):
        print(s, e, w, '/싸이클 발생! 탈락!')
        continue
    # 싸이클이 없으면 통과
    print(s, e, w)
    cnt += 1
    union(s, e)
    sum_weight += w

    # MST 구성이 끝나면(필요없는 간선 줄임)
    if cnt == V-1:
        break
    # if find_set(s) != find_set(e):
    #     cnt += 1
    #     union(s, e)
    #     sum_weight += w
    #     if cnt == V:  # MST 구성이 끝나면
    #         break

print(f'최소비용 = {sum_weight}')

