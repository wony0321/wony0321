import sys
sys.stdin = open('1234_input.txt')

T = 10
for tc in range(1, T+1):
    N, num = map(str, input().split())

    # 문자로 받아서 리스트에 각각의 숫자 넣기
    num_lst = list(num)

    stack = []

    for i in range(int(N)):
        if len(stack) == 0:
            stack.append(num_lst[i])
            continue
        if stack[-1] == num_lst[i]:
            stack.pop()
        else:
            stack.append(num_lst[i])

    print(f'#{tc} ', *stack, sep='')