


month = int(input())


dp = [0] * (month+1)

dp[1]= 1
dp[2]= 1
dp[3] = 2

'''链接：https://www.nowcoder.com/questionTerminal/1221ec77125d4370833fd3ad5ba72395?f=discussion
来源：牛客网

  ///关键是找到递推式 f(n)=f(n-1)+f(n-2) (n>=4)
    ///递推式的解释:对于第n个月的兔子数量：有两部分组成，
    ///一部分是上个月的兔子f(n-1)，另一部是满足3个月大的兔子
    ///会生一只兔子f(n-2)'''
for i in range(4,month+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[month])


'''a:一个月兔子数，b：两个月兔子数，c：三个月兔子个数'''
a= 1
b=0
c=0
i=1
while i<month:
    c += b
    b = a
    a = c
    i+= 1

print(a+b+c)