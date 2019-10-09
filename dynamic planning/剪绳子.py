'''
给你一根长度为n的绳子，请把绳子剪成m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]
可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

递归方程：
max_1 = max(max_1,max_ls[j]*max_ls[i-j])
i表示长度，就表示从哪里开始分割

初始状态：
max_ls【0】 = 0
max_ls【1】 = 1
max_ls【2】 = 2
max_ls【3】 = 3
max_ls【4】 = 4
'''

# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        max_ls = [0,1,2,3]
        for i in range(4,number+1):
            max_1 = 0
            for j in range(1,i):
                max_1 = max(max_1,max_ls[j]*max_ls[i-j])
            max_ls.append(max_1)
        return max_ls.pop()