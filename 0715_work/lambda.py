ls = []
L = ['True', 'False', 'True', 'False', 'True', 'False'] # 没必要加引号
L = [True, False, True, False, True, False] # 没必要加引号
NL = lambda x:'1' if x == True else '0'

# 列表表达式
ls = [NL(i) for i in L]
print(ls)

'''
for i in L:
    ls.append(NL(i))
print(ls)
'''
