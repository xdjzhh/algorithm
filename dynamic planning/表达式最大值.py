'''

类似矩阵链相乘

给你一个表达式，你可以通过在不同的地方添加括号从而改变式子的结果。比如1 + 2 * 3，如果是（1+2）*3结果是9，如果是1+2*3，结果是7，现在给你一个这样的式子，保证只有乘法和加法，但是也许会出现负数，求出这个式子通过不同的加括号方式，所能求得的最大结果。
Input

多组数据，每组数据第一行给出一个整数N(2<=N<=100)，是所给式子的整数个数，下面包含表达式，所有整数和符号之间都会相隔一个空格。
Output

对于每组测试数据输出一个给出式子能算出的最大值。
Sample Input

4
1 + 2 * 3 + -1

Sample Output

8


dp[i][j] 表示第i-j的数字间的最大值

初始状态：
    dp[0][0] = number[0]
    dp[i][i] = number[i]
    i<j

状态转移方程：
    dp[i][j] = max(dp[i][k]  (operation[k])  dp[k+1][j], mindp[i][k]  (operation[k])  mindp[k+1][j])  (i<=k<j)
    mindp[i][j] = min(mindp[i][k]  (operation[k])  mindp[k+1][j])  (i<=k<j)


'''
def operation(singal,value1,value2):
    if singal == '-':
        return value1 - value2
    if singal == '+':
        return value1 + value2
    if singal == '/':
        return value1/value2
    if singal == '*':
        return value1 * value2


def largest(number,signal):
    length = len(number)
    if length == 0:
        return 0
    if length == 1:
        return number

    dp = [[0]* length for i in range(length)]
    mindp = [[10000] * length for i in range(length)]
    for i in range(length):
        dp[i][i] = number[i]
        mindp[i][i] = number[i]
        if i < length-1:
            dp[i][i+1] = operation(signal[i], number[i], number[i+1])
            mindp[i][i+1] = operation(signal[i], number[i], number[i+1])

    for l in range(2,length):
        for i in range(length-l):
                j = i + l
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j],operation(signal[k],dp[i][k],dp[k+1][j]), operation(signal[k],mindp[i][k],mindp[k+1][j]))
                    mindp[i][j] = min(mindp[i][j],operation(signal[k],mindp[i][k],mindp[k+1][j]))
                    print(i,k,j)
                    print(mindp[i][j],mindp[i][k],mindp[k+1][j])
    print(dp)
    print(mindp)
    return dp[0][length-1]

if __name__ == '__main__':
    number = [1,2,3,-1]
    signal = ['+','*','+']
    number1 = [1,2,3,4,-1]
    signal1 = ['+','*','-','+']
    number2 = [1,2,3,6,1,2,3,5,7,2,8,9]
    signal2 = ['+','-','*','-','-','*','-','*','+','-','*']
    print(largest(number1,signal1))