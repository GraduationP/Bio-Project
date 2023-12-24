import numpy as np
import bisect

def IndexSorted(seq,ln):
    global index
    index = []
    for i in range(len(seq)-ln+1):
        index.append((seq[i:i+ln], i))
    index.sort() 
    return index

def query(t,p,index):
    keys = [r[0] for r in index]
    st = bisect.bisect_left(keys,p[:len(keys[0])])
    en = bisect.bisect(keys,p[:len(keys[0])])
    hits = index[st:en] 
    print(hits)
    l=[h[1] for h in hits ]
    offsets=[]
    for i in l:
        if t[i:i+len(p)]==p:
            offsets.append(i)
    return offsets


        