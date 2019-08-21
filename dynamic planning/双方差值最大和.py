'''
题意：
给定序列a[0],a[1]......a[n-1]
两个玩家A 和 B 轮流取数
每个人每次只能取第一个或最后一个
双方都要是自己的数和 最大
问先手是否必胜


确定状态：
f[i][j]
为一方先手在面对a[i],⋯,a[j]
这些数字时，能得到的最大的与对手的数字差：

f[i][j]     =      max(    a[i]−f[i+1][j]       ,         a[j]−f[i][j−1]   )

先手方                         f[i-1][j] 对手方              f[i][j-1]对手方
'''

def coins(lst):
    n=len(lst)
    f=[[0]*n for _ in range(n)]

    for i in range(n):
        f[i][i]=lst[i]

    for length in range(2,n+1):
        for i in range(n-length+1):
            j=i+length-1
            f[i][j]=max(lst[i]-f[i+1][j],lst[j]-f[i][j-1])
            print (lst)
            print ("f[{}][{}]=max({}-f[{}][{}],{}-f[{}][{}])".format(i,j,lst[i],i+1,j,lst[j],i,j-1))
            print ("f[{}][{}]={}\n".format(i,j,f[i][j]))

    return f[0][n-1]>=0

if __name__ == '__main__':
    print(coins([1,2,3,4,5]))
