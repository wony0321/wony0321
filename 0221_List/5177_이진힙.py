# 최소 힙 클래스로 구현
class MinHeap:
    def __init__(self, size):
        self.last = 0
        self.H = [0] * (size + 1)   # root가 1번 인덱스부터이기 때문에 +1
    def is_full(self):
        return self.last == len(self.H)
    def is_empty(self):
        return self.last == 0
    def insert(self, value):
        # 가득 차있다면
        if self.is_full():
            print('Full')
        else:
            # 마지막 위치에 값을 추가
            # 완전 이진 트리이기 때문에
            self.last += 1
            self.H[self.last] = value

            # 최소 힙 조건을 만족하기 위해
            # 만약 비교할 부모가 있다면 아래 반복
                # 자식 노드와 부모 노드의 값을 비교해서
                    # 부모 노드가 더 작다면 확정(반복 종료)
                    # 부모 노드가 더 크다면 자식의 값과 부모의 값을 교환
            child = self.last   # 막 추가된 위치의 값과 비교
            parent = child//2
            # 사실 parent라는 값 없어도 child 만으로도 코드 짤 수 있음(해보기)
            while parent:
                if self.H[parent] > self.H[child]:
                    self.H[parent], self.H[child] = self.H[child], self.H[parent]
                    # 교환된 부모를 다시 자식으로 변경하여 부모가 있는지 또 확인
                    child = parent
                    parent = child//2
                else:
                    break
    # 힙은 항상 root만 지울 수 있다.
    def pop_root(self):
        if self.is_empty():
            print('Empty')
        else:
            value = self.H[1]
            # root에 마지막 요소를 이동 시킴 (완전 이진트리를 유지)
            self.H[1] = self.H[self.last]
            # 마지막 요소 삭제
            self.H[self.last] = 0
            self.last -= 1

            # child와 parent는 인덱스 값
            # 최소 힙을 유지하기 위해 부모와 자식 값을 비교
            parent = 1
            # 자식(왼쪽, 오른쪽 자식 2개)이 존재하면 비교
            child = parent*2
            while child <= self.last:   # 마지막 원소 인덱스보다 작다면 자식이 존재
                if parent*2+1 <= self.last and self.H[child] > self.H[parent*2+1]:     # 오른쪽 자식이 존재한다면
                    # 자식들 중 더 작은 값을 부모와 비교해야 함
                    child = parent*2+1
                # 부모와 자식 값을 비교
                if self.H[parent] > self.H[child]:
                    self.H[parent], self.H[child] = self.H[child], self.H[parent]
                    parent = child # 부모 값 변경
                    child = parent*2 # 새로운 왼쪽 자식
                else:
                    break
        return value
    def get(self, node):
        return self.H[node]

import sys
sys.stdin = open('5177_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_heap = MinHeap(N)

    for i in range(N):
        min_heap.insert(arr[i])

    print(min_heap.H)
    # 마지막 노드의 조상 노드의 값의 합 구하기
    last = min_heap.last   # 인덱스 값
    # 조상을 찾자
    total = 0
    while last//2:
        parent = last//2
        total += min_heap.get(parent)
        last = parent
    print(f'#{tc} {total}')