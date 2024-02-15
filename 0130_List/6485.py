import sys
sys.stdin = open('6485_input.txt')

# 테스트 케이스의 숫자만 보고 짐작 하지말자
# 문제에 제시된 정보들 잘 확인하고 문제 풀자


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = [0] * 5001  # 5000번 정류장까지
    # N개의 노선을 정류장에 표시
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):  # 1<=A<=B<=5000 (이런거 적는 습관 기르자)
            counts[j] += 1

    P = int(input())
    busstop = [int(input()) for _ in range(P)]
    print(f'#{tc}', end = ' ')
    for i in busstop:  # 출력할 정류장 번호
        print(counts[i], end = ' ')
