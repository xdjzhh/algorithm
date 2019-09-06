'''

    State:
    dp[i][j]: 表示string[i...j]中的回文子序列长度

    Initial State:
    dp[i][i] == 1
    string[i] == string[i+1] : dp[i][i+1] == 2
    string[i] != string[i+1] : dp[i][i+1] == 1

    State Transition:

'''



def solution(s):
    dp = [[0] * len(s) for i in range(len(s))]
    print(dp)
    if not s:
        return 0

    n = len(s)


    # init
    for i in range(n):
        dp[i][i] = 1  # length 1
        if i < n-1:  # length 2
            if s[i] == s[i +1]:
                dp[i][i+1] = 2
            else:
                dp[i][i+1] = 1

    print(dp)
    for l in range(3,n+1):   #此处指的是子串长度范围从3开始    因为 1  2  在上循环已经初始化
        for i in range(n-l+1):
            j = i+l-1
            # dp[i + 1][j - 1] == l-2意思是 dp[i + 1][j - 1]必须是回文，若不是回文max(dp[i + 1][j], dp[i][j - 1])计算
            if (s[i] == s[j]) & (dp[i + 1][j - 1] == l-2):

                    dp[i][j] = max([dp[i][j], dp[i + 1][j - 1] + 2])

            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    print(dp)
    return dp[0][n-1]
    pass


if __name__ == '__main__':
    string = 'asddsaaaqd'
    print(solution(string))