import random
import record
def pole():
    f = open("Words.txt",encoding='utf8')
    d = []
    for i in range(97):
        d.append(f.readline())
    slmassive = [i for i in range(0,97)]
    random.shuffle(slmassive)
    slindex = 0
    zadslovo = d[slmassive[slindex]]
    bykvi = ['b1','b2','b3','b4','b5','b6','b7','b8','b9','b10','b11','b12','b13','b14','b15']
    for i in range(len(zadslovo)-1):
        bykvi[i] = '□'
    secretword = bykvi.count('□') * '□'
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
        if nowlife == 0 or (secretword).count('□') == 0 or slindex == 96:
            if slindex == 96:
                print('Слова исчерпаны ')
                break
            if nowlife == 0 :
                print('У вас закончились жизни')
                N = 0
                print('загаданное слово', newword)
                print('Хотите ли вы попробовать еще раз? :\n 1.Да \n 2.Нет ')
                ppppp = int(input())
                if ppppp == 1 :
                    print('Выберите уровень сложности : \n 1.Легкая \n 2.Средняя \n 3.Сложная')
                    oi = int(input())
                    if oi == 1:
                        nowlife = 7
                    if oi == 2:
                        nowlife = 5
                    if oi == 3:
                        nowlife = 3
                    slindex += 1
                    newword = d[slmassive[slindex]]
                    bykvi = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10', 'b11', 'b12', 'b13', 'b14',
                             'b15']
                    for i in range(len(newword)-1):
                        bykvi[i] = '□'
                    secretword = bykvi.count('□') * '□'
                else:
                    print("Игра окончена")
                    return ""
            else:
                print('Вы отгадали ')
                N+=1
                print('Ваш рекорд : ', record.record(N))
                print('Ваш текущий счет : ', N)
                print('Хотите ли вы еще раз сыграть? \n 1.Да \n 2.Нет')
                p = int(input())
                if p == 2:
                    print("игра окончена")
                    return ""
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
                    for i in range(len(newword)-1):
                        bykvi[i] = '□'
                    secretword = bykvi.count('□') * '□'
        print(secretword +'|'+'♥'+'x'+str(nowlife))
        print('Назовите букву или слово целиком')
        w = input()
        if len(w)==1:
            if newword.count(w) == 1:
                if w in newword:
                    indexbykvi = newword.index(w)
                    secretword = secretword[:indexbykvi] + str(w) + secretword[indexbykvi+1:]
            if newword.count(w) == 2:
                indexbykvi = newword.index(w)
                lastindexbykvi = newword.rindex(w)
                secretword = secretword[:indexbykvi] + str(w) + secretword[indexbykvi+1:]
                secretword = secretword[:lastindexbykvi] + str(w) + secretword[lastindexbykvi+1:]
            if newword.count(w) == 0:
                print('Неправильно.Вы теряете жизнь')
                nowlife-=1
        else:
            popo = 1
            for i in range(len(newword)-1):
                if w[i]!=newword[i]:
                    print('Неправильно')
                    nowlife = 0
                    popo = 0
                    break
                if popo == 1:
                    secretword = newword


