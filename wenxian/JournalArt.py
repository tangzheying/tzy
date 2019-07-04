file = open('./JournalArticle.txt', 'r', encoding='UTF-8')
nfile = file.read()
#print(nfile)
zidian = {}
yihang = nfile.strip().split('\n')
#print(yihang)
for i in yihang:
    #print(i)
    if i != '':
        # print(i.strip().split(' ',1))
        zidian[i.strip().split(':')[0].strip('{').strip('}')] = i.strip().split(':')[1]
#print(zidian)

print(zidian['Author'] + ',' + zidian['Title'] + '[' + 'J' + ']' + ',' + zidian['Journal'] + \
      ',' + zidian['Year'] + ',' + zidian['Volume'] + ',' + zidian['Pages'])