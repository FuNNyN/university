import random
def N(x):
    count = 0
    for i in range(x):
        a = random.randint(0,2) #vibor cheloveka
        b = random.randint(0,2) #priz
        if a==b:
            count+=1
    uy = count/x * 100
    procentsogl = 100-uy
    return procentsogl

