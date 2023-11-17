# -*- coding: cp1251 -*-
from dddd import N
from birthday import birth
print('Выберите парадокс : \n 1.Монти Холла \n 2.Дней рождений')
pick = int(input())
if pick == 1:
    print(N(int(input('Введите кол-во игр: '))), '%')
else:
    print(birth(int(input('Введите кол-во людей: ')),int(input('Введите кол-во попыток: '))))

