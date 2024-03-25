import sys
sys.stdin = open('6274_input.txt')

# 자율주행 자동차가 멈추지 않고, 시간 T 이내에 갈 수 있는 교차로의 수
# 단, 신호가 맞지 않으면 그 교차로에는 갈 수가 없다.
# 이동 경로에 있는 모든 교차로 개수 출력
# 한 번 갔던 교차로는 중복해서 세지 않음

N, T = map(int, input().split())
sign = [list(map(int, input().split())) for _ in range(N**2)]

print(sign)