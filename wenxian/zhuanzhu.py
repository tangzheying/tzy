f = open('../doc/practice1.enw', 'r', encoding = 'UTF-8')
data = f.readlines()
# print(n)
ls = []
Title = ''
Journal = ''
Year = ''
Volume = ''
Pages = ''
Auls = []
Author = ''
for i in data:
    if i.strip('\n') != '':
        strip_i = i.strip(' ').strip('\n')
        ls.append([strip_i.split(' ', 1)[0], strip_i.split(' ', 1)[1]])
for j in ls:
    if j[0] == '%T':
        Title = j[1]
    if j[0] == '%D':
        Year = j[1]
    if j[0] == '%A':
        # print(j[1])
        Auls.append(j[1])

# result = ','.join(Auls) + '.' + Title + '[M]' + '.' + 'Cambridge Univ. Pr' + ':' + ','.join(Auls) + ',' + Year
# print(result)
result = Auls + '.' + Title + '[M]' + '.' + 'Cambridge Univ. Pr' + ':' + Auls + ',' + Year
print(result)