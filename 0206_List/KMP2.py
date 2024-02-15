def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * M
    j = 0   # index for pat[]

    # preprocess the pattern (calculate lps[] array)
    compteLPSArray(pat, M, lps)

    i = 0
    while i < N:
        if pat[i] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print("Found pattern at index" + str(i-j))
            j = lps[j-1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1