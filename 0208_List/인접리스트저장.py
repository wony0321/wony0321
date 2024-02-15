'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# 주로 인풋은 간선(E) 정보와 정점(V) 정보를 같이 줌
# 인접 배열을 저장할 때는 간선의 정보를 이용해서 저장하면 됨
# 인접 배열을 초기화할 때는 정점 정보를 이용하면 됨
# 간선은 시작점과 도착점이 묶여 있는 것

# V: 정점의 개수, E: 간선의 개수
V, E = 7, 8
edge_list = list(map(int, input().split()))

# 정점 번호를 그대로 index로 사용하기 위해 +1을 함
adj_list = [[] for _ in range(V+1)]

for idx in range(E):
    start = edge_list[idx*2]
    end = edge_list[idx*2+1]

    adj_list[start].append(end)
    # 만약 양방향으로 저장해야 하는 경우
    # adj_list[end].append(start)

for i in range(V+1):
    print(adj_list[i])

'''
[]
[2, 3]
[4, 5]
[7]
[6]
[6]
[7]
[]
'''