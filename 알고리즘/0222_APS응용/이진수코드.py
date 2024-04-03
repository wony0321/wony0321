tar = 149
result = []

while tar != 0:
    result.append(tar%2)
    tar //= 2

result.reverse()
print(result)