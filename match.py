def match(seq,sub_seq):
    result = "Match at "
    x=-1
    for i in range(len(seq)-len(sub_seq)+1):
        if sub_seq==seq[i:i+len(sub_seq)]:
            result = result + ' ' + str(i)
    return result