
# push 함수(append랑 같은 기능)
def push(n):
    global top
    top += 1
    if top == size:
        print('Overflow!')
    else:
        stack[top] = n

top = -1
size = 10
stack = [0]*size  # 최대 10개 push

top += 1            # push(10)
stack[top] = 10
top += 1            # push(20)
stack[top] = 20

push(30)

while top >= 0:
    top -= 1
    print(stack[top+1])

# 재귀함수 이용해보기
def f2(n):
    n *= 2
    print(n)
def f1(c, d):
    e = c + d
    f2(e)

a = 10
b = 20
c = a + b
f1(a, b)

# 피보나치를 재귀함수로 구현
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(10))


# 재귀함수
def f(i, k):            # i: 현재위치, k: 목표
    if i == k:
        return
    else:
        print(arr[i])
        f(i+1, k)

arr = [10, 20, 30]
N = len(arr)
f(0, N)

# 피보나치 재귀함수
def fibo(n):
    global cnt
    cnt += 1
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
def fibo_memo(n):
    global cnt
    cnt += 1
    if n != 0 and memo[n] == 0:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]


cnt = 0
n = 7
print(fibo(n), cnt)
cnt = 0
memo = [0] * (n+1)
memo [0] = 0
memo [1] = 1
print(fibo_memo(n), cnt)
print(memo)