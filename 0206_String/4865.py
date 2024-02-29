import sys
sys.stdin = open('4865_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    # 각 str을 리스트로 만들기
    str1_lst = list(str1)
    str2_lst = list(str2)
    # 카운팅할 리스트 생성
    count = [0] * N

    # 각각의 리스트를 이중 for문 돌려서 비교
    for i in range(M):
        for j in range(N):
            if str2_lst[i] == str1_lst[j]:
                count[j] += 1

    # 가장 큰 값 추출
    max = 0
    for num in count:
        if num > max:
            max = num

    print(f'#{tc} {max}')