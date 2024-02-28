import sys
sys.stdin = open('5203_input.txt')

# 연속인 숫자가 3개 이상 = run
# 같은 숫자가 3개 이상 = triplet

def check(lst):
    counts = [0] * 10
    r = 0
    t = 0
    for i in range(len(lst)):
        counts[lst[i]] += 1
        for j in range(8):
            if counts[j] >= 1 and counts[j+1] >= 1 and counts[j+2] >= 1:
                r += 1
        for j in range(10):
            if counts[j] >= 3:
                t += 1
        if r > 0 or t > 0:
            return i+1
    return 0

T = int(input())
for tc in range(1, T+1):
    num_lst = list(map(int, input().split()))
    player1 = []
    player2 = []
    for n in range(len(num_lst)//2):
        player1.append(num_lst[n*2])
        player2.append(num_lst[n*2+1])

    p1 = check(player1)
    p2 = check(player2)

    if p1 > 0 and p2 > 0:
        if p1 <= p2:
            print(f'#{tc} 1')
        elif p1 > p2:
            print(f'#{tc} 2')
    elif p1 == p2 == 0:
        print(f'#{tc} 0')
    elif p1 == 0 and p2 > 0:
        print(f'#{tc} 2')
    elif p2 == 0 and p1 > 0:
        print(f'#{tc} 1')