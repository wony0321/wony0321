import sys
sys.stdin = open('18404_input.txt')

T = 1
def f(i, k):  # i는 인덱스 번호, k는 리스트 길이
    s = 0
    global cnt
    if i == k:
        for j in range(k):
            if bit[j]:
                s += arr[j]
        if s == 10:
            cnt += 1
    else:
        bit[i] = 1
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)
    return cnt

arr = list(map(int, input().split()))
N = len(arr)
bit = [0]*N     # bit[i]: arr[i]가 부분집합에 포함되었는지 나타내는 배열
cnt = 0         # 부분집합의 합이 10인걸 카운팅하기 위해 초기화
ans = f(0, N)         # bit[i]에 1 또는 0을 채우고, N개의 원소가 결정되면 부분집합을 출력

print(f'#{T} {ans}')