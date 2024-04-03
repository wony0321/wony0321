def construct_candidates(a, k, input, c):
    # a = [0, 0, 0, 0], k = 1, input = 3, c = [0, 0]
    global NMAX
    in_perm = [False] * NMAX
    # in_perm = [False, False, False, False]
    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    # c[0] = True
    # c[1] = False
    return ncandidates

def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    if k == input:
        for i in range(1, k+1):
            print(a[i], end=" ")
        print()
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        # a = [0, 0, 0, 0], k = 1, input = 3, c = [0, 0]
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)


MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
backtrack(a, 0, 3)