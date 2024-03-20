import sys
sys.stdin = open('1865_input.txt')

# person: 인원
# effi: 현재까지 누적 효율
def perm(person, effi):
    global max_effi
    # 종료 조건

    # 현재 효율이 최대 효율보다 이미 같거나 낮다면 더이상 볼 필요가 없음
    if max_effi >= effi:
        return

    if person == N:
        # print(work)
        # temp = 1
        # for w in work:
        #     temp *= w
        if max_effi < effi:
            max_effi = effi
        return
    # 일을 차례대로 하나씩 맡기
    for i in range(N):
        # 이미 누가 일을 맡았다면 넘어감
        if used[i]:
            continue
        # 누군가 맡지 않은 일이 있다면
        used[i] = 1         # 해당일을 맡고
        # work.append(work_lst[person][i] * 0.01)
        perm(person+1, effi * work_lst[person][i] * 0.01)    # 다음 사람 차례(효율도 같이 넘기자)
        # work.pop()
        used[i] = 0         # 새로운 일을 맡기 위해


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work_lst = [list(map(int, input().split())) for _ in range(N)]

    work = []   # 임시로 확인
    max_effi = 0    #최대 효율을 저장
    # 해당 일을 맡았는지 확인
    used = [0]*N
    perm(0, 1)  # 시작 효율은 100%

    print(f'#{tc} {max_effi*100:.06f}')

