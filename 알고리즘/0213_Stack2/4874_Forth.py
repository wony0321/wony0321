import sys
sys.stdin = open('4874_input.txt')

operator = ['*', '/', '+', '-']

T = int(input())
for tc in range(1, T+1):
    fx = list(map(str, input().split()))

    stack = []
    break_p = True

    for tk in fx:   # tk는 토큰
        if tk not in operator and tk != '.':
            stack.append(int(tk))
        elif tk in operator:
            if len(stack) > 1:
                pop1 = stack.pop()
                pop2 = stack.pop()
                if tk == '*':
                    stack.append(pop2*pop1)
                elif tk == '/':
                    stack.append(pop2//pop1)
                elif tk == '+':
                    stack.append(pop2+pop1)
                elif tk == '-':
                    stack.append(pop2-pop1)
            else:
                result = 'error'
                break_p = False
                break

    if break_p == True and len(stack) == 1:
        print(f'#{tc}', *stack)
    else:
        print(f'#{tc} {result}')