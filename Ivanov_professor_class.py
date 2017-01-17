import re


class Professor:
    def __init__(self, fullname, workplace, interest, telnum):
        self.fullname = fullname
        self.workplace = workplace
        self.interest = interest
        self.telnum = telnum

file = open('Professors.txt', 'r', encoding='utf-8')
text = file.read()
text = text.split('<div class="main content small">')

arr = []
for i in text:
    fullname = re.findall('title="(.+?)"', i, flags=re.DOTALL)
    workplace = re.findall('<a class="link" href=.+>(.+)</a>', i)
    interest = re.findall('<a class="tag".+?>(.+?)</a>', i, flags=re.DOTALL)
    telnum = re.findall('<span>(\+7.+?)</span>', i, flags=re.DOTALL)
    arr.append(Professor(fullname, workplace, interest, telnum))

for j in arr:
    print('ФИО:', ' '.join(j.fullname))
    print('Место работы:', ', '.join(j.workplace))
    print('Интересы:', ', '.join(j.interest))
    print('Номер телефона:', ' '.join(j.telnum))
    print()

file.close()
