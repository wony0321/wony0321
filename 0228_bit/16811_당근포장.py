import sys
sys.stdin = open('16811_input.txt')

def func(lev, start, N):
    if lev == 3:
        if sum(stack) == N:
            temp = sorted(stack)
            new_lst.append(temp)
        return
    for i in range(start, N//2+1):
        stack.append(i)
        func(lev+1, i, N)
        stack.pop()

T = int(input())
for tc in range(1, T+1):
    # N: 당근의 개수
    N = int(input())
    # 당근의 크기
    carrot = list(map(int, input().split()))
    carrot.sort()
    stack = []
    new_lst = []

    # 당근 포장 조건
        # 대, 중, 소 상자로 구분해 포장 -> 같은 크기는 같은 상자에
        # 한 상자에 N//2개 초과하는 당근 있어서는 안됨
        # 개수 차이가 최소가 되도록 -> 개수차이를 서류에 표시
        # 포장할 수 없는 경우에는 -1, 포장할 수 있으면 최소 당근 개수 차이 출력

    # 당근 리스트를 N//2 초과하지 않고 세 개(소중대)로 쪼개야 함
    # 쪼갠 뒤에 차이 비교
    # 세 수를 더해서 N이 되는 조합 찾으면 됨
    func(0, 1, N)

    count = [0]*31
    for size in carrot:
        count[size] += 1
    new_count = []
    for n in count:
        if n != 0:
            new_count.append(n)
    print(new_count)
    print(new_lst)

    ans = []
    check_lst = []
    for i in range(len(new_lst)):
        for j in range(3):
            check = 0
            for k in range(len(new_count)):
                if new_lst[i][j] < new_count[k]:
                    check = -1
                    break
            if check == 0:
                check_lst.append(new_lst[i])
                break
        # if check != -1:
        #     ans.append(new_lst[i][-1]-new_lst[i][0])
    print(check_lst)
    if ans:
        print(f'#{tc} {min(ans)}')
    else:
        print(f'#{tc} -1')