import sys
sys.stdin = open('18282_input.txt')

T = int(input())
for tc in range(1, T+1):
    test = input()
    N = len(test)

    stack = []

    # 함수 써서 해보기!!!!!
    # stack이 비어있을 때는 pop을 하지 않고, 차있으면 pop

    for i in range(N):
        if test[i] == ')':
            if len(stack) == 0:
                stack.append(None)
                # print(f'#{tc} -1')
                break
            else:
                stack.pop()
        elif test[i] == '(':
            stack.append('(')

    # 안 비어 있을 경우
    if stack:
        print(f'#{tc} -1')
    # 비었을 경우
    elif not stack:
        print(f'#{tc} 1')