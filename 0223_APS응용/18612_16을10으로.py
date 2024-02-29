import sys
sys.stdin = open('18612_input.txt')

# 2진수로 바꾼 뒤에 앞에 0b 떼고나서 4자리로 표현해주면서 0 추가
# while문을 써서

T = int(input())
for tc in range(1, T+1):
    hex_str = input().strip()
    dec_num = int(hex_str, 16)
    z_lst = []
    i = 0
    while hex_str[i] == '0':
        z_lst.append(0)
        i += 1
    bin_num = bin(dec_num)
    look = bin_num[2:]

    for i in range(0, len(bin_num), 7):
        find = look[i:i+7]
        z_lst.append(int(find, 2))
    print(f'#{tc}', *z_lst)
