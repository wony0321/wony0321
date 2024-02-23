# print(0b11011110 and 0b11011)
# print(0x4A3 or 25)
#
# print(int('11011110', 2))
# print(int('11011', 2))
# print(int('4A3', 16))

#KEY = 1004
#
# def encode_decode(n):
#     global KEY
#     return n ^ KEY
#
# num = 0b1101
# print(bin(num << 2))
# print(bin(num >> 2))

#num = 0b1
# t = 1
# for i in range(5):
#     print(bin(t), t)
#     t = t << 1

# N = str(bin(4))
# new_str = ''
# for n in N:
#     if n.isdecimal():
#         if n == 0:
#             new_str += '1'
#         else:
#             new_str += '0'
#     else:
#         continue
# print(new_str)

# N, M = map(int, input().split())

# N = 5
# M = 31
#
# def Test():
#     tar = M
#     for i in range(N):
#         if tar & 0x1 == 0:
#             return False
#         tar = tar >> 1
#     return True
# print(Test())

# bin_m = str(bin(M))
# bin_len = len(bin_m)
#
# cnt = 0
# for i in range(bin_len-1, bin_len-N-1, -1):
#     if bin_m[i] == '1':
#         cnt += 1
# if cnt == 5:
#     print("ON")
# else:
#     print("OFF")

n = 0.1

print(f'변수 값은 {n: .2f}입니다')
print(f'변수 값은 {n: .21f}입니다')



