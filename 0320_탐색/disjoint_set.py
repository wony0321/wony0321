# 1~6번까지 노드 존재
# 1. make-set
def make_set(n):
    # 자기 자신이 대표인 데이터 6개가 리스트로 생성
    return [i for i in range(n)]
    # 각각의 숫자는 무슨 의미? 대표자 인덱스를 의미함

# 1~6번까지를 사용하기 위해 7 입력(0번은 버림)
parents = make_set(7)

# 2. find_set: 대표자를 찾아보자! 너의 대표는 누구니?
# - 합치기 전에는 자기 자신이 대표자
# - 부모 노드를 보고, 부모 노드도 연결이 되어 있다면 다시 반복
# - 언제까지? 자기자신이 대표인 데이터를 찾을 때까지
def find_set(x):
    # 자기 자신이 대표이면 return
    if parents[x] == x:
        return x

    # 위의 조건이 걸리지 않았다 == 대표자가 따로 있다.
    return find_set(parents[x])

# 3. union: 자기자신을 가르키고 있던걸 연결해서 합치는 것
def union(x, y):
    # parents[y] = x라고 하면 연결된거임
    # 이미 연결되어 있는 친구들기리 한 번 더 연결 시도하면 문제가 생길 수도 있음
        # x <- y <- z 이면 z를 x에 바로 연결되면 안됨
    # cycle 체크하는 데에 쓰임
    x = find_set(x)
    y = find_set(y)

    # 이미 같은 집합에 속해있다면 continue
    if x == y:
        return

    # 다른 집합이라면 합침
    # 예) 더 작은 루트노드에 합쳐라
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 같은 집합에 속해 있는지를 확인하는 것
union(1, 3)
union(2, 3)
union(5, 6)

print(parents)

# Rank와 경로 압축도 공부해보기