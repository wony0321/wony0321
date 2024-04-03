import sys
sys.stdin = open('input.txt')

import heapq
from heapq import heappush, heappop
import math

# 엄청 큰 값 10억(누적 거리로 잡음)
INF = int(1e9)
# INF = math.inf

V, E = map(int, input().split())
start = 0   # 시작 노드 번호 지정 (문제에서 주어질 수도 있음)

# 인접 리스트
graph = [[] for _ in range(V)]
# 누적 거리를 저장할 변수
distance = [INF] * V

# 간선 정보 저장
for _ in range(E):
    # 출발, 도착, 가중치
    s, e, w = map(int, input().split())
    # graph[3] = [[3,4]]
    graph[s].append([w, e])

def dijkstra(start):
    pq = []

    # 시작점의 weight, node 번호를 한 번에 저장
    heapq.heappush(pq, (0, start))
    # 시작 노드 초기화(이거 안해주면 돌아와서 사이클 발생 가능)
    distance[start] = 0

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heapq.heappop(pq)

        # pq의 특성 때문에 더 긴거리가 미리 저장되어 있음
        # now가 이미 더 짧은 거리로 온 적이 있다면 pass
        if distance[now] < dist:
            continue

        # now에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            if new_dist >= distance[next_node]:
                continue

            # 누적 거리를 최단 거리로 갱신
            distance[next_node] = new_dist
            # next_node의 인접 노드들을 pq에 추가
            heapq.heappush(pq, (new_dist, next_node))

dijkstra(0)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(V):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("INF", end=' ')
    else:
        print(distance[i], end=' ')
