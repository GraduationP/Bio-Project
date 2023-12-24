import numpy as np

def Badchars(seq,sub_seq):
    result = 'Result: '
    count = []
    cn = 0
    table=np.zeros([4,len(sub_seq)])     
    row=["C","G","A","T"]
    for i in range (4):
        num=-1
        for j in range (len(sub_seq)):
            if row[i]==sub_seq[j]:
                table[i,j]=-1
                num=-1
            else:
                num+=1
                table[i,j]=num
    x=-1
    i=0
    while(i<len(seq)-len(sub_seq)+1):
        if sub_seq==seq[i:i+len(sub_seq)]:
            result = result + str(i) + ', '
            count.append(cn)
            x=i
        else:
            for j in range(i+len(sub_seq)-1,i-1,-1):
                if seq[j] != sub_seq[int(j-i)]:
                    k=row.index(seq[j])
                    i+=table[k,j-i]
                    cn += i
                    break
        i=int(i+1)
    return result, count
