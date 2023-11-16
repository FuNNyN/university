words = open("Words.txt",mode="w",encoding='utf8')
text =['книга\n','месяц\n','ручка\n','шарик\n','олень\n','носок\n']
words.writelines(text)
words.close()
slova = open("Words.txt",mode="r",encoding='utf8')