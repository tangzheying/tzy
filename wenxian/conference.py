def Analy(file, filetype):
    ls = []
    Title = ''
    BGTitle = ''
    Year = ''
    Auls = []
    if filetype == 'C':
        for i in nfile:
            #print(i)
            strip_i = i.strip(' ').strip('\n')
            ls.append([strip_i.split(' ', 1)[0], strip_i.split(' ', 1)[1]])
        #print(ls)
        #[序号] 作者.文献题名[R].报告地：报告会主办单位，年份.
        for j in ls:
            if j[0] == '%T':
                Title = j[1]
            if j[0] == '%B':
                BGTitle = j[1]
            if j[0] == '%D':
                Year = j[1]
            if j[0] == '%E':
                # print(j[1])
                Auls.append(j[1])
        Auls = ','.join(Auls)
        result = ','.join([Auls,
                          Title + '[A]',
                          BGTitle + '[C]',
                          Year])
        return result

if __name__ == '__main__':
    file = open('G:/Github_codes/tzy_cite_check/doc/conference.txt', 'r', encoding='UTF-8')
    nfile = file.readlines()
    result = Analy(nfile, 'C')
    print(result)