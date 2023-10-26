import random
count2yg = 0
count2neyg = 0
count1yg =0
count1neyg =0
def F(vibor):
    global count2yg
    global count2neyg
    global count1yg
    global count1neyg
    prize = random.randint(1,3)
    dveri = [0 for i in range(3)]
    dveri[prize-1] = 1
    d = 0
    c =[]
    #print(prize)
    while True:
        if prize == vibor:
            if prize == 1:
                c = [1, 2]
            if prize == 2:
                c = [0, 2]
            if prize == 3:
                c = [0, 1]
            o = random.choice(c)
            dveri.pop()
            #print(f'Ведущий открыл дверь под номер : {o + 1}')
            break
        elif dveri[d]!=1 and d!=vibor-1 and prize != vibor:
            dveri.pop(d)
            #print('Ведущий открыл дверь под номером',d+1)
            otkrito = d
            break
        else:
            d+=1
    while True:
        if vibor == prize and vibor ==1:
            vibor = 1
            prize = 1
            break
        if vibor == prize and vibor ==2:
            vibor = 1
            prize = 1
            break
        if vibor == prize and vibor ==3:
            vibor = 2
            prize = 2
            break
        if prize == 1 and vibor == 2:
            prize =1
            vibor = 2
            break
        if prize == 1 and vibor == 3:
            prize = 1
            vibor = 2
            break
        if prize == 2 and vibor == 3:
            prize = 1
            vibor = 2
            break
        if prize ==2 and vibor ==1:
            vibor = 1
            prize = 2
            break
        if prize ==3 and vibor ==1:
            vibor = 1
            prize = 2
            break
        if prize ==3 and vibor == 2:
            prize = 2
            vibor = 1
            break
    vopros = random.randint(1,2)
    if vopros == 2:   #ostalsya
        #print('Вы остались на месте')
        if prize == vibor:
            #print('Вы получили приз')
            count2yg +=1
        else:
            #print('Вы не получили приз')
            count2neyg +=1
    if vopros == 1:   #smenil
        #print('Вы сменили дверь')
        if vibor == 1:
            vibor = 2
        else:
            vibor = 1
        if prize == vibor:
            #print('Вы получили приз')
            count1yg+=1
        else:
            count1neyg+=1
            #print('Вы не получили приз')
    return ' '
print(F(random.randint(1,3)))






