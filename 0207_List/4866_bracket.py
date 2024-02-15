import sys
sys.stdin = open('4866_input.txt')

T = int(input())
for tc in range(1, T+1):
    test_str = input()
    N = len(test_str)

    stack = []

    for i in range(N):
        if test_str[i] == '(':
            stack.append('(')
        elif test_str[i] == '{':
            stack.append('{')
        elif test_str[i] == ')':
            stack.pop()
        elif test_str[i] == '}':
            stack.pop()

    if stack:
        print(f'#{tc} 0')
    elif not stack:
        print(f'#{tc} 1')