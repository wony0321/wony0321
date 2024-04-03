import sys
sys.stdin = open('input.txt', 'r')

# 우선순위 큐를 활용
from heapq import heappush, heappop

def prim(start):
    pq = []
    # visited 만들기(최소 비용 신장 트리)
    MST = [0] * V

    # 최소비용
    sum_weight = 0

    '''
    # 시작점 추가
    # [기존 BFS] 노드 번호만 관리
    # [PRIM] 우선 순위가 가중치에 따라 정렬(가중치가 낮으면 먼저 나와야 함)
        # -> 관리해야 할 데이터: 가중치, 노드 번호
        # -> 동시에 두가지 데이터 다루는 방법?
            # 1) class
            class Node:
                def __init__(self, num, weight):
                    self.num = num
                    self.weight = weight
            # 2) 튜플로 관리(이건 한 번에 3개 이상 데이터 저장에 좋지 않음)
    '''

    # (가중치, 노드 번호)
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)

        # print(now, MST)

        # 방문했다면 continue
        # 이걸 왜할까? BFS에서는 안하는데?
        # PRIM: 일단 pq에 넣고 방문은 안함 but BFS: 무조건 방문을 함
        # 우선순위 큐의 특성 상 더 먼거리로 가는 방법이 큐에 저장되어 있기 때문에
        # 기존에 이미 더 짧은 거리로 방문했다면 continue
        # 아래 예시를 그림으로 그려보면서 왜 방문했다면 continue해야하는지 파악하기
            # 노드 개수: 3, 간선 개수: 3
            # 0 1 100
            # 0 2 1
            # 1 2 2
        if MST[now]:
            continue

        # 방문 처리
        MST[now] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            # 갈 수 없다면 pass
            if graph[now][to] == 0 or MST[to]:
                continue

            # 이미 방문했다면 pass
            # if MST[to]:
                # continue
            heappush(pq, (graph[now][to], to))

    print(f'최소비용: {sum_weight}')


V, E = map(int, input().split())
# 인접 행렬로 저장
    # [실습] 인접 리스트로 저장
graph = [[0]*V for _ in range(V)]
for _ in range(E):
    # 출발, 도착, 가중치
    s, e, w = map(int, input().split())

    # 가중치 저장?
        # [기존] 3 -> 4로 갈 수 있다.
        # graph[3][4] = 1

        # [가중치 그래프] 3 -> 4로 가는 데 31이라는 비용이 든다
        # graph[3][4] = 31

    # 무방향 그래프
    graph[s][e] = w
    graph[e][s] = w

prim(0)