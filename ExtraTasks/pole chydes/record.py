def record(N):
    f = open("record.txt", mode='r')
    s = int(f.readline())
    if N>s:
        s = open("record.txt",mode="w",encoding='utf8')
        s.writelines(str(N))
        s.close()
        stroka = open("record.txt",mode="r",encoding='utf8')
        record = stroka.readline()
    else:
        record = s
    return record
print(record(int(input())))