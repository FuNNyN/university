import random
vsegodnei = 28*12
a = []
for i in range(vsegodnei):
    a.append(0)
def birth(N,C):
    count = 0
    for i in range(N):
        o = random.randint(0,vsegodnei-1)
        a[o]+=1
    for i in range(N):
        if a[i]>=2:
            count+=1
    print((count/C)*100,'%')
    return ''
# N - chelovek
# C - popitok
print(birth(250,100))
