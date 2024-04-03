import sys
sys.stdin = open('6019_input.txt')

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # 오차를 줄이기 위해 F 먼저 곱함
    T = D*F / (A+B)
    print(f'#{tc} {T}')