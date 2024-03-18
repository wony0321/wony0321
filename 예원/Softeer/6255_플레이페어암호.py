import string
import sys
sys.stdin = open('6255_input.txt')

# 플레이페어 암호: 알파벳으로 이루어진 문자열을 암호화
# 한 번에 두글자 단위로 암호화 진행
# I랑 J는 동일한 것으로 생각
# 같은 두 글자로 이루어진 쌍 -> 한글자+X를 넣고 새롭게 쌍 구성
# 만약 XX라면 Q를 넣는 것으로 해결
# 한 글자가 남을 때도 X를 붙여서 쌍 맞춤

# 1) 같은 행에 존재하면, 오른쪽으로 한칸 이동한 글자로 암호화
# 2) 1)의 경우 만족 X & 같은 열에 존재하면 한칸 이동한 걸로 암호화
# 3) 1), 2) 경우 모두 만족 X & 두 글자가 다른 행, 열에 존재하면, 열 서로 교환된 위치에 적힌 글자로 암호화

T = int(input())
for tc in range(1, T+1):
    message = input()
    # message_sep = [message[i:i+2] for i in range(0, len(message), 2)]
    key = input()
    alphabet_list = list(string.ascii_uppercase)
    key_arr = [[0]*5 for _ in range(5)]

    idx = 0
    for k in range(len(key)):
        if key[k] in alphabet_list and key[k] != 'J':
            key_arr[idx//5][idx%5] = key[k]
            alphabet_list.pop(alphabet_list.index(key[k]))
            idx += 1
    for a in alphabet_list:
        if a != 'J':
            key_arr[idx//5][idx%5] = a
            idx += 1

    message_lst = []
    m = 0
    while m < len(message):
        if m+1 < len(message):
            if message[m] == message[m+1] != 'X':
                message_lst.append(message[m]+'X')
                m += 1
            elif message[m] == message[m+1] == 'X':
                message_lst.append(message[m]+'Q')
                m += 1
            elif message[m] != message[m+1]:
                message_lst.append(message[m]+message[m+1])
                m += 2
        else:
            message_lst.append(message[m]+'X')
            m += 1

    # print(key_arr)
    # print(message_lst)
    for s in message_lst:
        for i in range(5):
            if s[0] in key_arr[i] and s[1] in key_arr[i]:
                idx = key_arr[i].index(s[0])
                print(key_arr[(idx+1)%5]+key_arr[(idx+2)%5])
            # if s[1] in key_arr[i]:
            #     print(i)