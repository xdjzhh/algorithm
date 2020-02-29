'''

题目描述
矩阵乘法的运算量与矩阵乘法的顺序强相关。
例如：

    A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵

计算A*B*C有两种顺序：（（AB）C）或者（A（BC）），前者需要计算15000次乘法，后者只需要3500次。

编写程序计算不同的计算顺序需要进行的乘法次数

输入描述:
输入多行，先输入要计算乘法的矩阵个数n，每个矩阵的行数，列数，总共2n的数，最后输入要计算的法则

输出描述:
输出需要进行的乘法次数

示例1
输入
复制
3
50 10
10 20
20 5
(A(BC))
输出
复制
3500
'''


number = int(input())

matrix_list = []
for i in range(number):
    string = list(map(int,input().split()))
    matrix_list.append(string)

operation = input()


def compute(L):
    if len(L) < 2:
        return 0
    if len(L) == 2:
        return L[0][0] * L[0][1] * L[1][1]
    elif len(L) >2:
        twosum = L[0][0] * L[0][1] * L[1][1]
        new_L = L[2:].insert(0,[L[0][0],L[1][1]])
        return twosum + compute(new_L)


stack = []
result = 0
for i in operation:
    if i != ')':
        if i.isalpha():
            stack.append(matrix_list.pop(0))
        else:
            stack.append(i)
    else:
        compute_list = []
        while True:
            if len(stack)  != 0:
                element = stack.pop()
                if element == '(':
                    break
                else:
                    compute_list.insert(0,element)
            else:
                break
        stack.append([compute_list[0][0],compute_list[-1][1]])
        result += compute(compute_list)
print(result)