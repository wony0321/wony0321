import sys
sys.stdin = open('input.txt')

# 순열(원본을 교환)
def perm(time):
    global max_value
    # 중복방지 가지치기 -> 하고 나면 정답 달라짐
    # 변경 횟수 별로 중복 숫자 관리해주면 됨
    value = int(''.join(number))
    if value in checked[time]:
        return
    # 체크된 적이 없다면
    checked[time].add(value)
    # 재귀 도는 횟수 == 숫자를 바꾸는 횟수
    # 변경 index는 따로 관리해야 함 (현재 코드에서는 배열의 길이만큼 변경횟수 동일함)
    # 바꾸는 위치가 N만큼 되면 재귀 종료 / N: 리스트의 길이
    if time == limit:
        # print(number)
        # 최댓값인지 확인
        # value = int(''.join(number))
        if max_value < value:
            max_value = value
        return
    else:
        # 교환할(변경) index를 위한 for문 하나 더 필요
        # i, j가 같아지는 순간은 자기 자신을 변경하게 됨
        for i in range(N):
            for j in range(i+1, N):
                number[i], number[j] = number[j], number[i]
                perm(time + 1)
                number[i], number[j] = number[j], number[i]


T = int(input())
for tc in range(1, T+1):
    # map(int, input().split())을 하게되면 number가 list로 변환하기 복잡해짐
    number, limit = input().split()
    number = list(number)
    limit = int(limit)

    N = len(number)
    max_value = 0

    # 중복을 방지하기 위한 set
    # 2차원으로 만들어서 반복 횟수별로 check
    checked = [set() for _ in range(limit+1)]

    perm(0)

    print(f'#{tc} {max_value}')