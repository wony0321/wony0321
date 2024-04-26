X = int(input())

# 어떤 줄인지 저장
line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X

print(f'{a}/{b}')