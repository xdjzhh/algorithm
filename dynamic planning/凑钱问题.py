
'''

凑钱问题与背包问题不同， 凑钱问题是按前的种类 依次排序 然后规划   比如： 1： 1  2：1 1|2  3：1 1 1|2 1 直到5  才会出现5：5

再例如  种类【1，7，9】17 组合为  1 7 9 因为达不到2*9的界限  所以是根据  17-9 = 8：1 7来界定 若达到界限  比如 18 ， 19  必定是 9 9 最佳

'''

def coins(coin_list,total):
    if coin_list ==[]:
        return 0
    if total < 0 :
        return 0

    dp = [100000 for i in range(total+1)]
    dp[0] = 0
    for i in coin_list:
        dp[i] = 1

    for i in range(1,total + 1):
        for j in range(3):
            # if (i >= coin_list[j]) & (dp[i] > dp[i-coin_list[j]] +1):
            #     dp[i] = dp[i - coin_list[j]] + 1
            if (i >= coin_list[j]):
                dp[i] = min(dp[i - coin_list[j]] + 1,dp[i])
    print(dp)
    return dp[total]


if __name__ == '__main__':
    print(coins([1,2,5],18))