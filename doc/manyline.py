def AnalyManyLine(nnf):
    ls = []
    for i in nnf:
        # print(i)
        for j in i.strip('').split('\n'):
            if j != '':
                # 这一句，如果不满足该条件，WXtype 就没有，然后WXtype 就会出现未定义
                if j.strip().split(' ', 1)[0] == '%0':
                    WXtype = j.strip().split(' ', 1)[1]
        # print(WXtype)
        if WXtype == 'Journal Article':
            NR = AnalysixJA(i, 2)
            ls.append(NR)
        # print(NR)
    return ls

def AnalysixJA(filenm, filetype):
    ls = []
    # zidian = {}
    Title = ''
    Journal = ''
    Year = ''
    Volume = ''
    Pages = ''
    Auls = []
    Author = ''
    yihang = filenm.strip().split('\n')
    if filetype == 1:
        for i in yihang:
            print(i)
            if i != '':
                # print(i.strip().split(':')[0].strip('{').strip('}'))
                ls.append([i.strip().split(':')[0].strip('{').strip('}'), i.strip().split(':')[1]])
        # print(ls)
        for j in ls:
            # print(j)
            # print(j[0])
            if j[0] == 'Title':
                Title = j[1]
                # print(Title)
                # print(j[1])

            if j[0] == 'Journal':
                Journal = j[1]

            if j[0] == 'Year':
                Year = j[1]

            if j[0] == 'Volume':
                Volume = j[1]

            if j[0] == 'Pages':
                Pages = j[1]

            if j[0] == 'Author':
                # print(j[1])
                Auls.append(j[1])

        geshi = Auls[0] + ',' + Auls[1] + ',' + Auls[2] + ',' + Title + '[' + 'J' + ']' + ',' + Journal + \
                ',' + Year + ',' + Volume + ',' + Pages
        # print(geshi)
        return geshi

    if filetype == 2:
        # print(yihang)
        for i in yihang:
            # print(i.strip().split(' ', 1))
            ls.append([i.strip().split(' ', 1)[0], i.strip().split(' ', 1)[1]])
        # print(ls)
        for j in ls:
            if j[0] == '%T':
                Title = j[1]
            if j[0] == '%J':
                Journal = j[1]
            if j[0] == '%D':
                Year = j[1]

            if j[0] == '%V':
                Volume = j[1]

            if j[0] == '%P':
                Pages = j[1]

            if j[0] == '%A':
                # print(j[1])
                Auls.append(j[1])
        geshi = Auls[0] + ',' + Auls[1] + ',' + Auls[2] + ',' + Title + '[' + 'J' + ']' + ',' + Journal + \
                ',' + Year + ',' + Volume + ',' + Pages
        # print(geshi)
        return geshi

    if filetype == 3:
        # print(yihang)
        for i in yihang:
            if '=' in i:
                # print(i.strip().strip(',').split('=')[0])
                # print(i.strip().strip(',').split('=')[1].strip('{').strip('}'))
                ls.append([i.strip().strip(',').split('=')[0],
                           i.strip().strip(',').split('=')[1].strip('{').strip('}')])
        # print(ls)
        for j in ls:
            if j[0] == 'title':
                Title = j[1]

            if j[0] == 'journal':
                Journal = j[1]

            if j[0] == 'year':
                Year = j[1]

            if j[0] == 'volume':
                Volume = j[1]

            if j[0] == 'pages':
                Pages = j[1]

            if j[0] == 'author':
                Author = j[1]
                # print(Author)

        geshi = Author + ',' + Title + '[' + 'J' + ']' + ',' + Journal + \
                ',' + Year + ',' + Volume + ',' + Pages
        # print(geshi)
        return geshi


if __name__ == '__main__':
    # 读取多行文件
    file = open('./manyline.enw', 'r', encoding='utf-8')
    nf = file.read()
    # print(type(nf))
    nnf = nf.strip('').split('\n\n')
    # print(nnf)
    result = AnalyManyLine(nnf)
    for i in result:
        print(i)
