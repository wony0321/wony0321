import sys
sys.stdin = open('5185_input.txt')

# 하드 코딩
bin_lst = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
hex_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
info = dict(zip(hex_lst, bin_lst))

T = int(input())
for tc in range(1, T+1):
    N, hex_str = map(str, input().split())

    print(f'#{tc}', end=' ')
    for s in hex_str:
        print(info[s], end='')
    print()