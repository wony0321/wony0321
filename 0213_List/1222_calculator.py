import sys
sys.stdin = open('1222_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    cal = input()

    top = -1
    stack = [0] * 1000
    postfix = ''
    # num = []
    #
    # for c in cal:
    #     if c == '+':
    #         top += 1
    #         stack[top] = c
    #     else:
    #         num.append(int(c))
    # for op in stack:
    #     if op == '+':
    #         pop1 = num.pop()
    #         pop2 = num.pop()
    #         num.append(pop1 + pop2)


    # for i in range(len(stack)-1, -1, -1):
    #     if stack[i] in operator:
    #         a = stack.pop()
    #         postfix += a
    #     else:
    #         stack.pop()

    # print(f'#{tc}', *num)