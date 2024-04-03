import sys
sys.stdin = open('4835_input.txt')
# 여기까지는 제출 시에는 삭제

# 가장 먼저 T(테스트 케이스) 확인!

T = int(input())  # Test Case가 주어지는 경우
#  T = 10
for tc in range(1, T+1): # 총 T개의 test 케이스가 존재
    # a = input() # input은 txt 파일 한 줄 씩 가져옴
    # print(a)
    # print(a.split()) # ['10', '3']
    # b = a.split()
    # print(list(map(int, b))) # [10, 3]
    # N, M = map(int, b)  # 정수의 개수 N과 구간의 개수 M이 주어짐 -> 언패킹
    N, M = map(int, input().split()) # N, M 가져오기
    arr = list(map(int, input().split())) # N개의 숫자를 리스트로 가져오기 (
    # 예시: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # 로직 작성
    sum_lst = []

    for i in range(0, N-M+1):
        num_sum = 0
        for j in range(0, M):
            num_sum += arr[i+j]
        sum_lst.append(num_sum)

    for i in range(len(sum_lst)-1, 0, -1):
        for j in range(0, i):
            if sum_lst[j] > sum_lst[j+1]:
                sum_lst[j], sum_lst[j+1] = sum_lst[j+1], sum_lst[j]

    answer = sum_lst[-1] - sum_lst[0]
    print(f'#{tc} {answer}')

    # 알고리즘이 힘드시거나 익숙하지 않으신 분들은
    # 반드시 주석을 적극 활용해주세요!
    # 주석에 어떤 값이 출력이 되고,
    # 주석에 어떤 동작을 작성해야 하는지
        # 동작 작성할 때는 최대한 세분화해서 동작 작성
        # 주석이 길어져도 상관 없음
    # 코드 작성에 길을 잃지 않을 정보를 주석에 작성하면
    # 보다 수월하게 코드를 작성할 수 있습니다.
    # 특히 길을 잃었을 때, 어떤 코드를 작성해야 할지 모를 때
    # 주석으로 차분히 정리하면 길이 보일거에요,,,

    # 출력하는 방법!!!!
    # print(f'#{tc} {계산한 결과값}')