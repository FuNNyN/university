from cod import *
f = open('new.txt',encoding = 'utf8')
count = len(words)
for i in range(count+1):
    print(f.readline())