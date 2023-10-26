import rasschet
import random
import calc
def N(kolvo):
    for i in range(kolvo-1):
        vibor = random.randint(1,3)
        rasschet.F(vibor)
N(int(input('кол-во игр \n')))
# ostalsya 2
# pomenyal 1
x1 = rasschet.count2neyg
x2 = rasschet.count1yg
y1 = rasschet.count2yg
y2 = rasschet.count1neyg
print(calc.Y(x1,x2,y1,y2),'%')
