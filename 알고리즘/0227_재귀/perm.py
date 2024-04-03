card = ['A', 'B', 'C']
r = 2   #r: 뽑으려는 개수
choice = [0]*r

def perm0(i, r):
    if i >= r:
        print(*choice)
        return
    else:
        for j in range(i, len(card)):
            choice[i] = card[j]     # append
            perm0(i+1, r)
            choice[i] = 0           # pop

# 중복 순열
def perm1(i, r):
    if i >= r:
        print(*choice)
        return
    else:
        for j in range(len(card)):
            choice[i] = card[j]     # append
            perm1(i+1, r)
            choice[i] = 0           # pop

# 중복되지 않은 순열
def perm2(i, r):
    if i >= r:
        print(*choice)
        return
    else:
        for j in range(len(card)):
            if used[j] == 0:    # 만약 카드가 사용되지 않았다면
                used[j] = 1     # 사용 처리
                choice[i] = card[j]     # 선택카드에 추가(append)
                perm2(i+1, r)
                choice[i] = 0           # 선택카드에서 제외(pop)
                used[j] = 0             # 미사용 처리

# 원본변경순열
def perm3(i, r):
    if i >= r:
        print(*card[:r])
        return
    else:
        for j in range(i, len(card)):
            card[i], card[j] = card[j], card[i]
            perm3(i + 1, r)
            card[i], card[j] = card[j], card[i]

perm0(0, r)
print('----' * 10)
perm1(0, r)
print('----' * 10)
used = [0]*len(card)
perm2(0, r)
print('----' * 10)
perm3(0, r)