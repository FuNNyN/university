# -*- coding: cp1251 -*-
from dddd import N
from birthday import birth
print('�������� �������� : \n 1.����� ����� \n 2.���� ��������')
pick = int(input())
if pick == 1:
    print(N(int(input('������� ���-�� ���: '))), '%')
else:
    print(birth(int(input('������� ���-�� �����: ')),int(input('������� ���-�� �������: '))))

