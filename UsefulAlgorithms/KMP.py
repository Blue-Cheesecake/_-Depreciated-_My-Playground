# given the word w[0..n-1]  and patttern par[0..m-1]
# write a function search that prints all occurrences of pat[] in w[]
# complexity : O(n)


def KMPsearch(pat, txt):
    N = len(txt)
    M = len(pat)
    # length of lps should be equal to length of pattern
    # lps array : Longest prefix that is alos suffix
    lps = [0] * M
    computeLPSArray(pat, M, lps)
    i = 0  # index of text
    j = 0  # index of pat
    while i < N:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == M:
            # print i - j
            # continue to search further till the end of text input
            print(i-j)
            j = lps[j-1]


def computeLPSArray(pat, M, lps):
    len = 0
    i = 1
    # the first must equal to 0 (there are no prefix and suffix )
    lps[0] = 0
    while i < M:
        if pat[i] == pat[len]:
            lps[i] = len + 1
            len += 1
            i += 1

        else:
            if len != 0:
                # reset to calculate correctly (prevent overlapping)
                len = lps[len-1]
            else:
                lps[i] = 0
                # go to the next
                i += 1


KMPsearch('eet', 'leetcode')
