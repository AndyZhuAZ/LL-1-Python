# LL(1)语法表驱动分析器
import prettytable as pt


def read(self):  # 读文件到list
    with open(self) as result:
        r = []
        for i in result.readline():
            r.append(i)
        r[-1] = '$'  # 终结符
        # r.pop()
        # r.append('$')
        return r


def addTable(stack, inputList, info):
    a = stack
    a.reverse()
    b = ''.join(a)
    c = inputList
    c.reverse()
    d = ''.join(c)
    # print(b, d, info)
    table.add_row([b, d, info])
    a.reverse()
    c.reverse()


def erro(stack, inputList, type):
    addTable(stack, inputList, 'erro:'+type)
    # print('erro')


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

    table = pt.PrettyTable()
    table.field_names = ['栈', '剩余输入', '输出']
    table.padding_width = 3
    table.align['栈'] = "r"
    table.align['剩余输入'] = "r"
    table.align['输出'] = 'l'
    addTable(stack, inputList, '')
    while stack[-1] is not '$':
        if stack[-1] is 'E':
            if inputList[-1] is 'i' or inputList[-1] is '(':
                stack.pop()
                stack.append('E\'')
                stack.append('T')
                addTable(stack, inputList, 'E-TE\'')
            elif inputList[-1] is '$':
                stack.pop()
                addTable(stack, inputList, 'input null')
            else:
                stack.pop()
                erro(stack, inputList, 'E no found i or (')
        if stack[-1] is 'E\'':
            if inputList[-1] is '+':
                stack.pop()
                stack.append('E\'')
                stack.append('T')
                stack.append('+')
                addTable(stack, inputList, 'E\'-+TE\'')
            elif inputList[-1] is ')' or inputList[-1] is '$':
                stack.pop()
                # stack.append('ε')
                addTable(stack, inputList, 'E\'-ε')
            else:
                stack.pop()
                erro(stack, inputList, 'E\' no found + )')
        if stack[-1] is 'T':
            if inputList[-1] is 'i' or inputList[-1] is '(':
                stack.pop()
                stack.append('T\'')
                stack.append('F')
                addTable(stack, inputList, 'T-FT\'')
            elif inputList[-1] is '$':
                stack.pop()
                addTable(stack, inputList, 'input null')
            else:
                stack.pop()
                erro(stack, inputList, 'T no found i (')
        if stack[-1] is 'T\'':
            if inputList[-1] in ['+','(','$']:
                stack.pop()
                # stack.append('ε')
                addTable(stack, inputList, 'T\'-ε')
            elif inputList[-1] is '*':
                stack.pop()
                stack.append('T\'')
                stack.append('F')
                stack.append('*')
                addTable(stack, inputList, 'T\'-*FT\'')
            else:
                stack.pop()
                erro(stack, inputList, 'T\' no found + （ *')
        if stack[-1] is 'F':
            if inputList[-1] is 'i':
                stack.pop()
                stack.append('i')
                addTable(stack, inputList, 'F-i')
            elif inputList[-1] is '(':
                stack.pop()
                stack.append(')')
                stack.append('E')
                stack.append('(')
                addTable(stack, inputList, 'F-(E)')
            elif inputList[-1] is '$':
                stack.pop()
                addTable(stack, inputList, 'input null')
            else:
                stack.pop()
                erro(stack, inputList, 'F no found i ( ')
        if stack[-1] in ['i', '+', '*', '(', ')']:
            if inputList[-1] in ['i', '+', '*', '(', ')']:
                stack.pop()
                inputList.pop()
                if stack[-1] is inputList[-1]:
                    addTable(stack, inputList, '')
                else:
                    erro(stack, inputList, 'no match')
        # if stack[-1] is 'i':
        #     if inputList[-1] is 'i':
        #         stack.pop()
        #         inputList.pop()
        #         addTable(stack, inputList, '')
        # if stack[-1] is '+':
        #     if inputList[-1] is '+':
        #         stack.pop()
        #         inputList.pop()
        #         addTable(stack, inputList, '')
        # if stack[-1] is '*':
        #     if inputList[-1] is '*':
        #         stack.pop()
        #         inputList.pop()
        #         addTable(stack, inputList, '')
        # if stack[-1] is '(':
        #     if inputList[-1] is '(':
        #         stack.pop()
        #         inputList.pop()
        #         addTable(stack, inputList, '')
        # if stack[-1] is ')':
        #     if inputList[-1] is ')':
        #         stack.pop()
        #         inputList.pop()
        #         addTable(stack, inputList, '')
    print(table)
    # print(a)
    # print(stack[-1])
    #
    # print(inputList)
