import sys
sys.stdin = open('1213_reverse_input.txt')

T = 10

# for tc in range(1, T+1):
#     len_str = int(input())  # 찾아야 하는 회문의 길이
#     str_lst = [list(map(str, input())) for _ in range(8)] # 알파벳 2차원 리스트 만들기
#
#     cnt = 0  # 회문의 개수 카운팅
#
#     # 세로(행 우선)
#     for i in range(8):
#         s_i = ''
#         for j in range(8):
#             ori_str_1 = str_lst[i][j]
#             s_i += ori_str_1
#         for idx in range(len_str, 9):  # 각 줄에서 회문의 길이만큼의 단어 뽑기
#             ans_str_1 = s_i[idx-len_str:idx]
#             rev_str_1 = ans_str_1[::-1]  # 회문인지 확인하기 위해 뒤집어보기
#             if rev_str_1 == ans_str_1:
#                 cnt += 1
#
#     # 가로(열 우선)
#     for j in range(8):
#         s_j = ''
#         for i in range(8):
#             ori_str_2 = str_lst[i][j]
#             s_j += ori_str_2
#         for idx in range(len_str, 9):
#             ans_str_2 = s_j[idx-len_str:idx]
#             rev_str_2 = ans_str_2[::-1]
#             if rev_str_2 == ans_str_2:
#                 cnt += 1
#
#     print(f'#{tc} {cnt}')

def is_pelindrome(string):
    M = len(string)     # 같은 값이 나오는 함수 실행은 한 번만 하면 됨
    # return string == string[::-1]
    for idx in range(M//2+1):
        if string[idx] != string[M-1-idx]:
            return False  # 반복을 돌다가 하나라도 틀리면 return False
    return True # 모든 반복을 다 돌았다면 return True

for tc in range(1, T+1):
    N = 8   # 문자열의 개수
    M = int(input())    # 찾아야하는 문자열 개수
    arr = [input() for _ in range(N)]
    count = 0   # 몇개 있는지 카운드
    # 행, 열 탐색으로 길이가 M인 문자열을 만들자
    for outer in range(N):
        for inner in range(N-M+1):
            row_str = ''
            col_str = ''
            for idx in range(M):
                row_str += arr[outer][inner+idx]    # 행 문자
                col_str += arr[inner+idx][outer]    # 열 문자

            # 회문인지 판별
            # print(row_str, col_str)
            # if is_pelindrome(row_str):
            #     count += 1
            # if is_pelindrome(col_str):
            #     count += 1
            # 혹은 아래와 같이 해도 가능
            count += is_pelindrome(row_str) + is_pelindrome(col_str)

    print(f'#{tc} {count}')