import sys
sys.stdin = open('4834_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 카드 장 수
    num_lst = list(map(int, input()))  # N 개의 숫자 리스트

    counts = [0] * 10  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for num in num_lst:
        counts[num] += 1

    max = counts[0]
    idx_save = 0

    for idx in range(10):
        if counts[idx] >= max:
            max = counts[idx]
            idx_save = idx

    print(f'#{tc} {idx_save} {max}')