import random

def r():
    num = random.randint(0, 2)
    if num == 0:
        rdn = random.randint(97, 122)
        s = chr(rdn)
    elif num == 1:
        rdn = random.randint(0, 999)
        s = str(rdn)
    else:
        rdn = random.random()
        s = str(rdn)
    return s

def main(num=100):
    result = []
    for i in range(num):
        s = r()
        result.append(s)
    return result

if __name__ == '__main__':
    r = main()
