import sys
sys.stdin = open('input.txt')

# 남학생: 스위치 번호가 받은 수의 배수이면 스위치 상태 바꿈
# 여학생: 받은 번호의 스위치를 중심으로 스위치 상태가 좌우 대칭 & 가장 많은 스위치

# 입력1: 스위치 개수 (100 이하)
N = int(input())

# 입력2: 각 스위치의 상태

# 1: 스위치 켜져 있음, 0: 스위치 꺼져있음
S = list(map(int, input().split()))

# 학생 수 (100이하)
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())

    # 남학생이면
    if sex == 1:
        i = 1
        while num*i <= N:
            if S[num*i-1] == 1:
                S[num*i-1] = 0
            else:
                S[num*i-1] = 1
            i += 1

    # 여학생이면
    else:
        idx = num - 1
        if S[idx] == 1:
            S[idx] = 0
        else:
            S[idx] = 1
        j = 1
        while 0 <= idx-j and idx+j < N:
            if S[idx-j] == S[idx+j]:
                if S[idx-j] == 1:
                    S[idx-j] = 0
                    S[idx+j] = 0
                else:
                    S[idx-j] = 1
                    S[idx+j] = 1
                j += 1
            else:
                break

for i in range(0, len(S), 20):
    print(*S[i:i+20])

