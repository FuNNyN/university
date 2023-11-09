import random
def birth(N,C):
    ncount = 0
    for i in range(C):
        vsegodnei = 28 * 12
        a = []
        for i in range(vsegodnei):
            a.append(0)
        count = 0
        for i in range(N):
            o = random.randint(0,vsegodnei-1)
            a[o]+=1
        for i in range(vsegodnei):
            if a[i]>=2:
                count+=1
        if count >=1:
            ncount+=1
    print((ncount/C)*100,'%')
    return ''
# N - chelovek
# C - popitok
