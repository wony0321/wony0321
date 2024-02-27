import sys
sys.stdin = open('5188_input.txt')

def f(i, N):
    if i == N-1:
        print(choice)
        return
    for j in range(N):
        choice.append(j)
        f(i+1, N)
        choice.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    choice = []
    f(0, N)

