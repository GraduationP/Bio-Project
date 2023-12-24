# Naive Pattern

def search(pat, txt):
    M = len(pat)
    N = len(txt)
    result = 'Search result: '
    global count
    global cnt
    cnt = [0,0]
    count = ''
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
            cnt.append(i)
            count = count + str(i-cnt[-1]-1) + ', ' 
            result = result + str(i) + ' '
    return result