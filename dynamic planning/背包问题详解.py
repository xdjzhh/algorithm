
'''

有n个物品，它们有各自的体积和价值，现有给定容量的背包，如何让背包里装入的物品具有最大的价值总和？

capacity : C
w: w0,w1,w2,w3
v: v0,v1,v2,v3

三个变量  i：前i个物品组合    j： 体积   dp【】【】：Value值

初始化： dp[i][i] = 0
        if j < w[i] : d[i][j] = d[i-1][j]

状态转移：
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
        第一种是第i件商品没有装进去，第二种是第i件商品装进去了。没有装进去很好理解，就是V(i-1,j)；装进去了怎么理解呢？如果装进去第i件商品，
        那么装入之前是什么状态，肯定是V(i-1,j-w(i))。V(i-1,j-w(i))就是前面决策造成的一种状态，后面的决策就要构成最优策略。两种情况进行比较，得出最优。


        当i=1时：
            dp[1][j] = max(dp[0][j],dp[0][j-w[1]]+v[1]) 无论j多大   只放入 第一个物品

'''

def bagv(w,v,capacity):   #01背包    每个物品只能放入一次
    dp = [[0]*(capacity+1) for i in range(len(w))]

    for i in range(len(w)):
        dp[i][0] = 0

    for i in range(1,len(w)):
        for j in range(1,capacity+1):
            if j < w[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
    print(dp)
    return dp[len(w)-1][capacity]



def bagn(w,v,capacity):    #完全背包，所有物品无限次数放入
    dp = [[0]*(capacity+1) for i in range(len(w))]

    for i in range(len(w)):
        dp[i][0] = 0

    for i in range(1,len(w)):
        for j in range(1,capacity+1):
            for k in range(int(j//w[i])+1):
                if k == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-k*w[i]]+k*v[i])
    print(dp)
    return dp[len(w)-1][capacity]

    pass




if __name__ == '__main__':
    capacity = 8
    w = [0,2,3,4,5]
    v = [0,3,4,5,6]
    print(bagv(w,v,capacity))
    print(bagn(w, v, capacity))