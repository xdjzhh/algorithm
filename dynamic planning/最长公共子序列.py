'''


最长公共子序列和最长公共子字符串是有区别的，公共子序列里的元素可以不相邻，但是公共子字符串必须是连接在一起的。

dp[i][j] : 最长公共子序列长度   i：前i个字符   j：前j个字符

初始状态：
    dp[0][0] = 0

状态转移方程：
if a[i] = b[j]:
    dp[i][j] = dp[i-1][j-1] + 1
else:
    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

'''

def longest(string1,string2):
    dp = [[0]* (len(string2)+1) for i in range(len(string1)+1)]

    dp[0][0] = 0
    if (len(string1) == 0) or (len(string2) == 0):
        return 0

    for i in range(1,len(string1)+1):
        for j in range(1,len(string2)+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[len(string1)][len(string2)]

    pass



if __name__ == '__main__':
    string1 = 'asdasdasdffggb'
    string2 = 'asdasdffggv'
    print(longest(string1,string2))