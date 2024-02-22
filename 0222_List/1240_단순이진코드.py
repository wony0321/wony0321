import sys
sys.stdin = open('1240_input.txt')

code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T+1):
    # N: 배열의 세로 크기, M: 배열의 가로 크기
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    # 암호가 시작되는 r, c 찾기
    r = 0
    c = 0
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                r = i
                c = j
                break

    # 암호 부분
    password = arr[r][c-55:c+1]

    # 암호 알아내기
    pass_num = []
    j = 0
    for i in range(8):
        s = ''
        for _ in range(7):
            s += password[j]
            j += 1
        pass_num.append(code[s])

    odd = 0
    even = 0
    hap = 0
    for i in range(1, len(pass_num)+1):
        if i % 2 != 0:
            odd += pass_num[i-1]
        else:
            even += pass_num[i-1]
        hap += pass_num[i-1]

    if (odd*3 + even) % 10 == 0:
        print(f'#{tc} {hap}')
    else:
        print(f'#{tc} 0')