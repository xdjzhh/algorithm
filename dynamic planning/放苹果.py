'''

题目描述
题目描述

把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。


输入

每个用例包含二个整数M和N。0<=m<=10，1<=n<=10。


样例输入

7 3


样例输出

8

输入描述:
输入两个int整数

输出描述:
输出结果，int型

示例1
输入
复制
7 3
输出
复制
8
'''

m, n = list(map(int, input().split()))


def recurse(m, n):
    '''recurse(0,n)是有效的 意味 有n个苹果n个盘子，在每个盘子里放一个后得到的结果，然而recurse(m,0)是无效的，所以m可以为0 n不能为0'''
    if m < 0 or n <= 0:
        return 0
    if m == 1:
        return 1
    if n == 1:
        return 1
    return recurse(m, n - 1) + recurse(m - n, n)


number = recurse(m, n)
print(number)