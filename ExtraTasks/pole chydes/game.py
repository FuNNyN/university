import random
import record
f = open("Words.txt",encoding='utf8')
d = []
for i in range(6):
    d.append(f.readline())
slmassive = [0,1,2,3,4,5]
random.shuffle(slmassive)
slindex = 0
zadslovo = d[slmassive[slindex]]
b1 = '□'
b2 = '□'
b3 = '□'
b4 = '□'
b5 = '□'
print('Выберите уровень сложности : \n 1.Легкая \n 2.Средняя \n 3.Сложная')
oi = int(input())
if oi == 1:
    nowlife = 7
if oi == 2:
    nowlife = 5
if oi == 3:
    nowlife = 3
newword = zadslovo
N = 0
while True:
    if nowlife == 0 or (b1+b2+b3+b4+b5).count('□') == 0 or slindex == 4:
        if slindex == 4:
            print('Слова исчерпаны ')
            break
        if nowlife == 0 :
            print('У вас закончились жизни')
            N = 0
            break
        else:
            print('Вы отгадали ')
            N+=1
            print('Ваш рекорд : ', record.record(N))
            print('Ваш текущий счет : ', N)
            print('Хотите ли вы еще раз сыграть? \n 1.Да \n 2.Нет')
            p = int(input())
            if p == 2:
                print("игра окончена")
                break
            else:
                print('Выберите уровень сложности : \n 1.Легкая \n 2.Средняя \n 3.Сложная')
                oi = int(input())
                if oi == 1:
                    nowlife = 7
                if oi == 2:
                    nowlife = 5
                if oi == 3:
                    nowlife = 3
                slindex+=1
                newword = d[slmassive[slindex]]
                b1 = '□'
                b2 = '□'
                b3 = '□'
                b4 = '□'
                b5 = '□'
    print(b1+b2+b3+b4+b5+'|'+'♥'+'x'+str(nowlife))
    print('Назовите букву или слово целиком')
    w = input()
    if len(w)==1:
        c =(b1+b2+b3+b4+b5).count('□')
        if w == newword[0]:
            b1 = b1.replace('□',w)
        if w == newword[1]:
            b2 = b2.replace('□',w)
        if w == newword[2]:
            b3 = b3.replace('□',w)
        if w == newword[3]:
            b4 = b4.replace('□',w)
        if w == newword[4]:
            b5 = b5.replace('□',w)
        if c == (b1+b2+b3+b4+b5).count('□'):
            print('Неправильно.Вы теряете жизнь')
            nowlife-=1
    else:
        if w[0] == newword[0] and w[1] == newword[1] and w[2] == newword[2] and w[3] == newword[3] and w[4] == newword[4]:
            b1 = newword[0]
            b2 = newword[1]
            b3 = newword[2]
            b4 = newword[3]
            b5 = newword[4]
        else:
            print('Неправильно.Вы теряете жизнь')
            nowlife -= 1

