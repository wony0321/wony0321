import sys
sys.stdin = open('4839_input.txt')

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    # 전체 쪽 수, 쪽 번호 a, 쪽 번호 b

    page_lst = []

    for p in range(1, P+1):
        page_lst.append(p)

    # 이진 탐색 써서, 이긴 사람의 이름 (A 또는 B) 출력, 비기면 0

    def binarySearch(lst, P, page):
        # 구간 초기화
        cnt = 0
        left = 0
        right = P - 1
        while left <= right:  # 검색 구간이 유효하면 반복
            c = (left + right) // 2  # 중앙 페이지 수 인덱스
            if lst[c] == page:  # 검색 성공
                return cnt
            elif lst[c] > page:  # 중앙값이 키보다 크면
                right = c - 1
                cnt += 1
            else:  # 키보다 작으면
                left = c + 1
                cnt += 1
        # return -1  # 검색 실패

    A_cnt = binarySearch(page_lst, P, Pa)
    B_cnt = binarySearch(page_lst, P, Pb)

    if A_cnt < B_cnt:
        print(f'#{tc} A')
    elif A_cnt > B_cnt:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')