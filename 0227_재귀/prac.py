
# 중복 순열
# for a in range(1, 4):
#     for b in range(1, 4):
#         for c in range(1, 4):
#             for d in range(1, 4):
#                 print(a, b, c, d)

#def KFC(x):
#     print(x)
#     x += 1
#     KFC(x)
#
# KFC(0)

# 기저조건은 6
# def f(x):
#     if x == 6:
#         return
#     print(x, end=' ')
#     f(x+1)
#     print(x, end=' ')
#
# f(0)

# path = []
# def run(level):
#     if level == 2:
#         # 기저조건(마지막 레벨)일 때, 출력
#         print(path)
#         return
#     for i in range(3):
#         path.append(i)
#         run(level+1)
#         path.pop()
# run(0)

path = []
# def run(x):
#     if x == 3:
#         print(*path)
#         return
#     for i in range(1, 7):
#         path.append(i)
#         run(x+1)
#         path.pop()
# run(0)


path = []
used = []
N = 0

def type_1(x):
    if x == N:
        print(path)
        return
    for i in range(1, 7):
        path.append(i)
        type_1(x+1)
        path.pop()

def type_2(x):
    if x == N:
        print(path)
        return
    for i in range(1, 7):
        # 이미 방문을 했던거라면 continue
        if used[i] == True:
            continue
        used[i] = True
        path.append(i)
        type_2(x+1)
        path.pop()
        used[i] = False

# False 말고 0으로 초기화해도 ok
used = [False for _ in range(7)]
N, type = map(int, input().split())

if type == 1:
    type_1(0)
if type == 2:
    type_2(0)

# path = []
# cnt = 0
#
# def KFC(x, sum):
#     global cnt
#     if sum > 10:
#         return
#     if x == 3:
#         # print(f'{path} = {sum}')
#         cnt += 1
#         return
#     for i in range(1, 7):
#         path.append(i)
#         KFC(x+1, sum+i)
#         path.pop()
#
# KFC(0, 0)
# print(cnt)

# def KFC(x):
#     if x == 3:
#         return
#     for i in range(2):
#         KFC(x+1)
#         print(f'{x} #{i}')
# KFC(0)