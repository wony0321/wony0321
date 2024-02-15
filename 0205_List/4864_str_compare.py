import sys
sys.stdin = open('4864_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()  # len: 4, 4, 12
    str2 = input()  # len: 10, 10, 20

    if str1 in str2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


    # start = 0
    # cnt = 0
    # for end in range(len(str1), len(str2)):
    #     if str2[start:end] == str1:
    #         cnt += 1
    #         start += 1
    #     else:
    #         start += 1
    #         continue
    #
    # if cnt > 0:
    #     print(1)
    # else:
    #     print(0)
