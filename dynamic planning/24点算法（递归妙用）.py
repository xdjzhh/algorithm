'''
题目描述
问题描述：给出4个1-10的数字，通过加减乘除，得到数字为24就算胜利
输入：
4个1-10的数字。[数字允许重复，但每个数字仅允许使用一次，测试用例保证无异常数字]
输出：
true or false

输入描述:
输入4个int整数

输出描述:
返回能否得到24点，能输出true，不能输出false

示例1
输入
复制
7 2 1 10
输出
复制
true
'''



number_list = list(map(int,input().split()))

def compute(L,value):
    if value < 1:
        return False
    if len(L) == 1 :
        return L[0] == value
    for i in range(len(L)):
        new_L = L[:i] + L[i+1:]
        if compute(new_L,value+L[i]) or compute(new_L,value-L[i]) or compute(new_L,value*L[i]) or compute(new_L,value/L[i]):
            return True
    return False

print(compute(number_list,24))
