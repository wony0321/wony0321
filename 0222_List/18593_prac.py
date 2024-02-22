import sys
sys.stdin = open('18593_input.txt')

T = int(input())
for tc in range(1, T+1):
    # 비트 문자열의 입력 개수
    N = int(input())
    num_lst = []
    for _ in range(N):
        num_lst.extend(list(map(int, input().strip())))

    ans_lst = []

    i = 0
    while i < len(num_lst):
        ans = 0
        j = 7
        for idx in range(i, i+7):
            j -= 1
            if num_lst[idx] == 1:
                ans += 2**j
        i += 7
        ans_lst.append(ans)

    print(f'#{tc}', *ans_lst)