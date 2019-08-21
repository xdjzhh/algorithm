


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
            if (i >= coin_list[j]) & (dp[i] > dp[i-coin_list[j]] +1):
                dp[i] = dp[i - coin_list[j]] + 1
    print(dp)
    return dp[total]


if __name__ == '__main__':
    print(coins([1,2,5],18))