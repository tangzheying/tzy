def AnalysixJA(filenm):
    yihang = filenm.strip().split('\n')
    for i in yihang:
        #print(i)
        if i != '':
            #print(i.strip().split(':')[0].strip('{').strip('}'))
            ls.append([i.strip().split(':')[0].strip('{').strip('}'),i.strip().split(':')[1]])
    #print(ls)
    for j in ls:
        #print(j)
        #print(j[0])
        if j[0] == 'Title':
            title = j[0]

        if j[0] == 'Journal':
            Journal = j[0]

        if j[0] == 'Year':
            Year = j[0]

        if j[0] == 'Volume':
            Volume = j[0]

        if j[0] == 'Pages':
            Pages = j[0]

        if j[0] == 'Author':
            #print(j[1])
            #--这里Auls 不应该做为全局变量，应该为函数内变量---#
            Auls.append(j[1])
    return title





if __name__ == '__main__':
    file = open('./JournalArticle.txt', 'r', encoding='UTF-8')
    nfile = file.read()
    ls = []
    zidian = {}
    Auls = []
    Title = ''
    Journal = ''
    Year = ''
    Volume = ''
    Pages = ''
    AnalysixJA(nfile)
    #print(Auls[0] + ',' + Title + '[' + 'J' + ']' + ',' + Journal + \
          #',' +Year + ',' + Volume + ',' + Pages)
    print(Auls[0] + ',' + Auls[1] + ',' + Auls[2])