import sys
sys.stdin = open('1213_string_input.txt', encoding='UTF-8')

T = 10
for tc in range(1, T+1):
    test_num = int(input())
    p_str = input()     # 찾을 패턴 텍스트
    t_str = input()  # 전체 텍스트
    N = len(p_str)      # 찾을 패턴의 길이
    M = len(t_str)   # 총길이

    cnt = 0

    for i in range(M-N+1):
        if t_str[i:i+N] == p_str:
            cnt += 1
    print(f'#{tc} {cnt}')