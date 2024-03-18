import sys
sys.stdin = open('6250_input.txt')

def check(idx, r, rank, sort_rank):
    while idx < N:
        if idx - 1 == 0:
            rank[sort_rank[idx-1][1]] = r
        if sort_rank[idx-1][0] == sort_rank[idx][0]:
            rank[sort_rank[idx][1]] = rank[sort_rank[idx-1][1]]
            r += 1
        else:
            r += 1
            rank[sort_rank[idx][1]] = r
        idx += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    total_scores = [[0, i] for i in range(N)]
    rank_sum = [0]*N
    for _ in range(3):
        rank_lst = [0]*N
        score = list(map(int, input().strip().split()))
        curr_score = []
        for i, n in enumerate(score):
            total_scores[i][0] += n
            curr_score.append((n, i))
        score_sort = sorted(curr_score, reverse=True)
        check(1, 1, rank_lst, score_sort)
        print(*rank_lst)

    sort_total = sorted(total_scores, reverse=True)
    check(1, 1, rank_sum, sort_total)
    print(*rank_sum)