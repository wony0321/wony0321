import sys
sys.stdin = open('1989_input.txt')

# 회문이란 뒤로 읽어도 앞으로 읽어도 똑같은 단어
# 회문인 경우 1, 아니면 0 출력

T = int(input())

for tc in range(1, T+1):
    tc_str = input()
    reverse_str = tc_str[::-1]

    if tc_str == reverse_str:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')