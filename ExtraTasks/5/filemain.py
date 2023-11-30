filename = input('Введите название файла : ')
def name_file(word):
    a = open(f"{word}", mode='w')
    r = ['3\n','12\n','23\n','42\n']
    a.writelines(r)
    return a.name
print('\nНазвание файла : ')
print(name_file(filename +'.txt'))
def read_file():
    file = open(f"{filename}.txt")
    return file.read()
print('Читка файла : ')
print(read_file())
def vivod_file():
    file = open(f"{filename}.txt")
    f = int(file.readline())
    d = []
    a = []
    for i in range(f):
        d.append(file.readline().splitlines())
    for i in range(f):
        a.append(int(d[i][0]))
    return a
print('Возвращение файла : ')
print(vivod_file())