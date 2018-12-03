# LL(1)文法的递归下降分析程序
a=0

def read(self):  # 读文件到list
    with open(self) as result:
        r = []
        for i in result.readline():
            r.append(i)
        return r


def e():
    print('E→TE′  ',expression[a])
    t()
    e1()


def e1():
    global a
    if expression[a] is '+':
        print('E′→+TE′', expression[a])
        # global a
        a= a+1
        t()
        e1()
    else:
        print('E′→ε    ')
    # return self


def t():
    print('T→FT′  ',expression[a])
    f()
    t1()


def t1():
    global a
    if expression[a] is '*':
        print('T′→*FT′', expression[a])
        # global a
        a = a + 1
        f()
        t1()
    else:
        print('T′→ε   ')
    # return self


def f():
    global a
    # print('F→(E)|i',expression[a])
    if expression[a] is '(':
        a = a + 1
        e()
        if expression[a] is ')':
            print('F→(E) ', expression[a])
            # global a
            a = a + 1
        else:print('erro')
    elif expression[a] is 'i':
        print('F→i    ', expression[a])
        # global a
        a = a + 1
    else:print('erro')


if __name__ == '__main__':
    # global a
    expression = read('test')
    e()
