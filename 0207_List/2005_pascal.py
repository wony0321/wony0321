import sys
sys.stdin = open('2005_input.txt')

# # def pascal(n):
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#     lst = [1]
#     for i in range(4):
#         lst.extend(lst)
#         if
#
# # print(lst)

def pascal(row, col):
    if row == col or col == 0:
        return 1
    else:
        return pascal(row-1, col-1) + pascal(row-1, col)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')
    for row in range(N):
        for col in range(row+1):
            # row가 0일때 하나, row가 1일때 두개,,
            # N*N이 나오면 안되기 때문에 N만큼 반복이 아니라 row_!
            print(pascal(row, col), end=' ')
        print()



