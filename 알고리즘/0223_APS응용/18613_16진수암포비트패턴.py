import sys
sys.stdin = open('18613_input.txt')

code = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011': 4, '110111': 5, '001011': 6, '111101': 7, '011001': 8, '101111': 9}

T = int(input())
for tc in range(1, T+1):
    hex_str = input().strip()
    dec_num = int(hex_str, 16)
    bin_num = bin(dec_num)

    look = '00' + bin_num[2:]

    print(f'#{tc}', end=' ')
    i = 0
    while i < len(look)-6:
        c = look[i:i+6]
        if c in code:
            print(code[c], end=' ')
            i += 6
        else:
            i += 1
    print()


