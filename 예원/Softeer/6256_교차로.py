import sys
sys.stdin = open('6256_input.txt')

check = {'A': 'D', 'B': 'A', 'C': 'B', 'D': 'C'}
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # car = [list(map(str, input().split())) for _ in range(N)]
    # print(car)
    car_dict = {}
    time_list = []
    for _ in range(N):
        t, w = map(str, input().split())
        time_list.append([w, int(t)])
        if int(t) not in car_dict:
            car_dict[int(t)] = [w]
        else:
            car_dict[int(t)].append(w)
    print(car_dict)
    turn = 0
    ans = []
    for k, v in car_dict.items():
        if len(v) == 1:
            ans.append(k)
        elif len(v) == 2:
            if check[v[0]] == v[1]:
                time_list[turn][1] += 1
            if check[v[1]] == v[0]:

        elif len(v) == 4:

        for road in v:
            if check[road] in v:
                time_list[turn][1] += 1
            else:
                ans.append(time_list[turn][1])
            turn += 1

    print(ans)
    print(time_list)
    # print(ans)
