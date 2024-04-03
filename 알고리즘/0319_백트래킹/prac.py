# 백트래킹
# 완전탐색(base) + 가지치기(볼 필요없는 조건)
# 가능성이 없는(볼 필요 없는) 경우의 수를 제거하는 기법
# 코딩 테스트를 위해서는 재귀를 연습해라!

# 중복된 순열
# 1~3까지 숫자 배열
# 111, 112, 113, 121, 122, 123 ... 332, 333

# 재귀함수는 특정 시점으로 돌아오는게 핵심!
# 재귀 함수 팁: 파라미터는 바로 작성하는게 아니라 구조를 먼저 잡으면 자연스럽게 필요한 변수들이 보인다.

arr = [i for i in range(1, 4)]
visited = [0]*3

# 조합
# 123, 132, 213, 231, 312, 321

def dfs(level):
    # 기저 조건
    # 이 문제에서는 3개를 뽑았을 때까지 반복
    if level == 3:
        print(*visited)
        return

    # 들어가기 전
    # 다음 재귀 호출
        # 다음에 갈 수 있는 곳들은 어디인가를 신경써주어야 함
        # 이 문제에서는 1, 2, 3 세 가지(arr의 길이만큼) 경우의 수가 존재
    # visited[level] = 1
    # dfs(level + 1)
    #
    # visited[level] = 2
    # dfs(level + 1)
    #
    # visited[level] = 3
    # dfs(level + 1)

    # 조합 다 뽑기
    # for i in range(level, len(arr)):
    #     visited[level] = arr[i]
    #     dfs(level+1)

    # 갈 수 있는 후보군
    for i in range(len(arr)):
        # 여기는 못가!(가지치기)
        # 백트래킹 코드 팁
        # 갈 수 없는 경우를 활용
        # 아래 코드처럼 갈 수 없을 때 continue
        if arr[i] in visited:
            continue

        visited[level] = arr[i]
        dfs(level+1)
        # 갔다와서 할 로직
        # 기존 방문을 초기화 해주어야 함
        visited[level] = 0

        # 가지치기의 시간복잡도? 계산하기가 너무 힘들다! 최악의 경우는 완전 탐색임
            # 1) 완탐 경우의 수
            # 2) 가지치기해서 대략적인 감소 예측

dfs(0)