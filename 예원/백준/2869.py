# A: 낮에 올라가는 높이(+)
# B: 밤에 미끌어지는 높이(-)
# V: 나무 막대 높이(총길이)

A, B, V = map(int, input().split())

# 이게 계속 A-B로 가다가 정상 오르기 직전(A로만 올라갈 수 있날)에는 A로만 가는게 문제임

left = (V%(A-B))
if left != 0:
    day = V//(A-B)+left
else:
    day = (V-A)//(A-B)+1

print(day)