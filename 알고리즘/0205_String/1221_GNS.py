import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for tc in range(1, T+1):
    num_str, num_len = map(str, input().split())
    lst = list(map(str, input().split()))

    str_lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    new_lst = []

    for i in str_lst:
        for j in lst:
            if i == j:
                new_lst.append(j)
    nums = ' '.join(new_lst)
    print(num_str, '\n', nums)


    # 딕셔너리에 넣어서 하는 방법도 있음