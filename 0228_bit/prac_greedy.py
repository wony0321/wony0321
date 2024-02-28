# 샤워 빨리 끝내는 사람이 먼저 해야 누적합 최소가 될 것
# student = {'A': 15, 'B': 30, 'C': 50, 'D': 10}
# person = [15, 30, 50, 10]
# n = len(person)
# person.sort()
# sum = 0
# left_person = n-1
# for turn in range(n):
#     time = person[turn]
#     # 누적합 = 남은 사람 * 시간
#     sum += left_person*time
#     left_person -= 1
# print(sum)

# # 물건 3개
# n = 3
# # knapsack 30 kg
# target = 30
# # (kg, price)
# things = [(5, 50), (10, 60), (20, 140)]
# # kg당 가격으로 내림차순
# things.sort(key = lambda x: (x[1] / x[0]), reverse=True)
#
# sum = 0
#
# for kg, price in things:
#     per_price = price/kg
#     # 만약 가방에 남은 용량이 얼마 되지 않는다면, 물건을 잘라 가방에 넣고 끝난다
#     if target < kg:
#         sum += target * per_price
#         break
#
#     sum += price
#     target -= kg
# print(int(sum))

# 회의가 짧게 끝나는 것부터 배정 -> 그게 끝나면 바로 시작할 수 있는 것으로 배정


# 가장 일찍 시작하고 끝나는 시간이 짧은 것 골라야 함
n = 10
time = [(1, 4), (3, 5), (1, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (2, 13), (12, 14)]
# time.sort(key = lambda x: (x[1], x[0]), reverse= False)
for i in range(n):
    for j in range(i+1, n):
        if time[i][1] > time[j][1]:
            time[i], time[j] = time[j], time[i]
print(time)


