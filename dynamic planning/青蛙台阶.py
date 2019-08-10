'''
1）一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
    初始状态：f(n)
    初始化： f(0)=0,f(1)=1,f(2)=2
    假设第一次分别跳1阶，2阶。。。。。。。n阶，那么有:
    f(n) = f(n-1)+f(n-2)+f(n-3).....f(n-n)
    f(n-1) = f(n-2)+f(n-3).....f(n-n)
    每一个f  都有多种跳法


2）一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

    如上所述f(n) = f(n-1)+f(n-2)，分别指代第一次跳1阶和2阶的情况。 可以得出就是一个fibonacci数列

'''



def jumpfloor(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = 1
    for i in range(3,n+1):
        result = 2*result
    return result

if __name__ == '__main__':
    print(f'jump case :{jumpfloor(10)}')