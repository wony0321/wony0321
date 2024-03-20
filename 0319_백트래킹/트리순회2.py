arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

# 코딩테스트에서는 간단하게
nodes = [[] for _ in range(14)]
for i in range(0, len(arr), 2):
    parent_node = arr[i]
    child_node = arr[i+1]
    nodes[parent_node].append(child_node)

for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)
'''
[[None, None], [2, 3], [4, None], [5, 6], [7, None], [8, 9], [10, 11], [12, None], [None, None], [None, None], [None, None], [13, None], [None, None], [None, None]]
'''


# 중위순회 구현
def inorder(nodeNum):
    # 갈 수 없다면 skip
    if nodeNum == None:
        return
    # 왼쪽으로 갈 수 있다면 진행
    inorder(nodes[nodeNum][0])
    # 오른쪽으로 갈 수 있다면 진행
    print(nodeNum, end=' ')
    inorder(nodes[nodeNum][1])

inorder(1)