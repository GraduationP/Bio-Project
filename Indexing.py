# Python3 program for Naive Pattern
# Searching algorithm


def search(pat, txt):
    M = len(pat)
    N = len(txt)
    result = 'Search result: '
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        while (j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == M):
            result = result + str(i) + ' '
    return result
    


# Driver's Code
if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"

    # Function call
    search(pat, txt)

# This code is contributed Omnia Fathy