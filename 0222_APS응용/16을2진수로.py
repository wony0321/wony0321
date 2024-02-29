# 하드 코딩
bin_lst = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
hex_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# T = 0
# if 'A':
#     T = 10
#     bin_lst[T]

ans_1 = '73'
ans_2 = 'AB'

def hex_to_bin(ans):
    ans_lst = []
    for a in ans:
        if a in hex_lst:
            idx = hex_lst.index(a)
            ans_lst.append(bin_lst[idx])
    print(*ans_lst)

hex_to_bin(ans_1)
hex_to_bin(ans_2)
