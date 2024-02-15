import sys
sys.stdin = open('4873_input.txt')

T = int(input())
for tc in range(1, T+1):
    test_str = input()
    N = len(test_str)

    stack = []

    for i in range(N):
        if len(stack) == 0:
            stack.append(test_str[i])
            continue
        if stack[-1] == test_str[i]:
            stack.pop()
        else:
            stack.append(test_str[i])

    ans = len(stack)
    print(f'#{tc} {ans}')