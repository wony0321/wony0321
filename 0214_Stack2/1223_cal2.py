import sys
sys.stdin = open('1223_input.txt')

operator = ['*', '/', '+', '-']
icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 스택 밖에서의 우선순위
isp = {'(':0, '*':2, '/':2, '+':1, '-':1} # 스택 안에서의 우선순위

T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = input()

    top = -1
    stack = [0] * N
    postfix = ''

    # postfix에 후위 표기
    for tk in fx:
        if tk in operator:
            if top == -1:
                top += 1
                stack[top] = tk
            else:

                if isp[stack[top]] < icp[tk]:
                    top += 1  # push
                    stack[top] = tk
                elif isp[stack[top]] >= icp[tk]:
                    while top != -1 and isp[stack[top]] >= icp[tk]:  # top 원소의 우선순위가 낮을 때까지 pop

                        top -= 1
                        postfix += stack[top + 1]
                    top += 1
                    stack[top] = tk
        else:
            postfix += tk
    while top != -1:
        top -= 1
        postfix += stack[top+1]

    # 숫자만 있는 배열 만들기

    num = []

    for p in postfix:
        if p == '*':
            pop1 = int(num.pop())
            pop2 = int(num.pop())
            num.append(pop2*pop1)
        elif p == '+':
            pop1 = int(num.pop())
            pop2 = int(num.pop())
            num.append(pop2+pop1)
        else:
            num.append(p)

    print(f'#{tc}', *num)