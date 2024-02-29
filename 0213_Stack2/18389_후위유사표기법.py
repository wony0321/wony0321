import sys
sys.stdin = open('18389_input.txt')

operator = ['*', '/', '+', '-']

T = int(input())
for tc in range(1, T+1):
    fx = input()
    # 2+3*4/5

    top = -1
    stack = [0] * 100
    postfix = ''

    for tk in fx:
        if tk in operator:
            top += 1  # push
            stack[top] = tk
        else:  # 피연산자인 경우
            postfix += tk
    for i in range(len(stack)-1, -1, -1):
        if stack[i] in operator:
            a = stack.pop()
            postfix += a
        else:
            stack.pop()
    print(f'#{tc} {postfix}')