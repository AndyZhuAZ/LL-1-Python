# LL(1)语法表驱动分析器


def read(self):  # 读文件到list
    with open(self) as result:
        r = []
        for i in result.readline():
            r.append(i)
        r.pop()
        r.append('$')  # 终结符
        return r


def erro():
    print('erro')

if __name__ == '__main__':
    inputList = read('test')  # 输入串
    # ['i', '+', 'i', '*', 'i', '$']
    inputList.reverse()
    # ['$', 'i', '*', 'i', '+', 'i']

    stack = []  # 栈
    stack.append('$')
    stack.append('E')
    # stack.append('E\'''')
    # ['$', 'E']

    print(stack, inputList)
    while stack[-1] is not '$':
        if stack[-1] is 'E':
            if inputList[-1] is 'i' or '(':
                stack.pop()
                stack.append('E\'')
                stack.append('T')
                print(stack,inputList,'E-TE\'')
            elif inputList[-1] is '$':
                stack.pop()
                print(stack, inputList, 'input null')
            else:erro()
        if stack[-1] is 'E\'':
            if inputList[-1] is '+':
                stack.pop()
                stack.append('E\'')
                stack.append('T')
                stack.append('+')
                print(stack,inputList,'E\'-+TE\'')
            elif inputList[-1] is ')' or '$':
                stack.pop()
                # stack.append('ε')
                print(stack,inputList,'E\'-ε')
            else:erro()
        if stack[-1] is 'T':
            if inputList[-1] is 'i' or '(':
                stack.pop()
                stack.append('T\'')
                stack.append('F')
                print(stack,inputList,'T-FT\'')
            elif inputList[-1] is '$':
                stack.pop()
                print(stack, inputList, 'input null')
            else:erro()
        if stack[-1] is 'T\'':
            if inputList[-1] is '+' or '(' or '$':
                stack.pop()
                # stack.append('ε')
                print(stack,inputList,'T\'-ε')
            elif inputList[-1] is '*':
                stack.pop()
                stack.append('T\'')
                stack.append('F')
                stack.append('*')
                print(stack,inputList,'T\'-*FT\'')
            else:erro()
        if stack[-1] is 'F':
            if inputList[-1] is 'i':
                stack.pop()
                stack.append('i')
                print(stack, inputList, 'F-i')
            elif inputList[-1] is '(':
                stack.pop()
                stack.append(')')
                stack.append('E')
                stack.append('(')
                print(stack, inputList, 'F-(E)')
            elif inputList[-1] is '$':
                stack.pop()
                print(stack, inputList, 'input null')
            else:erro()
        if stack[-1] is 'i':
            if inputList[-1] is 'i':
                stack.pop()
                inputList.pop()
                print(stack, inputList)
        if stack[-1] is '+':
            if inputList[-1] is '+':
                stack.pop()
                inputList.pop()
                print(stack, inputList)
        if stack[-1] is '*':
            if inputList[-1] is '*':
                stack.pop()
                inputList.pop()
                print(stack, inputList)
        if stack[-1] is '(':
            if inputList[-1] is '(':
                stack.pop()
                inputList.pop()
                print(stack, inputList)
        if stack[-1] is ')':
            if inputList[-1] is ')':
                stack.pop()
                inputList.pop()
                print(stack, inputList)
        # if stack[-1] is 'i' or '+' or '*' or '(' or ')':
        #     if inputList[-1] is 'i' or '+' or '*' or '(' or ')':
        #         stack.pop()
        #         inputList.pop()
        #         print(stack, inputList)
            # print(stack.pop(),inputList.pop())
            # stack.pop()
            # inputList.pop()
        # if stack[-1] is '+':
        #     print(stack.pop(), inputList.pop())
        # if stack[-1] is '*':
        #     print(stack.pop(), inputList.pop())
        # if stack[-1] is '('
        # print(stack[-1])
        # stack.pop()
    # a=stack.pop()

    # print(a)
    # print(stack[-1])
    #
    # print(inputList)
