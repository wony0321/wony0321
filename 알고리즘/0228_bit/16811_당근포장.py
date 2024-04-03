import sys
sys.stdin = open('16811_input.txt')


def func(lev, start, N):
    if lev == 3:
        if sum(stack) == N:
            temp = sorted(stack)
            new_lst.append(temp)
        return
    for i in range(start, N // 2 + 1):
        stack.append(i)
        func(lev + 1, i, N)
        stack.pop()


T = int(input())
for tc in range(1, T + 1):
    # N: 당근의 개수
    N = int(input())
    # 당근의 크기
    carrot = list(map(int, input().split()))
    carrot.sort()
    stack = []
    new_lst = []

    func(0, 1, N)

    count = [0] * 31
    for size in carrot:
        count[size] += 1
    new_count = []
    for n in count:
        if n != 0:
            new_count.append(n)
    new_count.sort()

    ans = []
    for i in range(len(new_lst)):
        j = 0
        check = 0
        for j in range(1, 4):
            if new_lst[i][-j] < new_count[-j]:
                check = -1
                break
        if check == 0:
            ans.append(new_lst[i][-1] - new_lst[i][0])

    if ans:
        print(f'#{tc} {min(ans)}')
    else:
        print(f'#{tc} -1')