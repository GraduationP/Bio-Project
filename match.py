def match(seq,sub_seq):
    result = "Match at "
    global count 
    count = -1
    for i in range(len(seq)-len(sub_seq)+1):
        if sub_seq==seq[i:i+len(sub_seq)]:
            result = result + ' ' + str(i)
            break
        else:
            count += 1
    return result, count

