'''

假设序列S和T的长度分别为m和n, 两者的编辑距离表示为edit[m][n]. 则对序列进行操作时存在以下几种情况:

a, 当S和T的末尾字符相等时, 对末尾字符不需要进行上述定义操作中(亦即"编辑")的任何一个, 也就是不需要增加计数. 则满足条件: edit[m][n] = edit[m - 1][n - 1].
b, 当S和T的末尾字符不相等时, 则需要对两者之一的末尾进行编辑, 相应的计数会增加1.
b1, 对S或T的末尾进行修改, 以使之与T或S相等, 则此时edit[m][n] = edit[m - 1][n - 1] + 1;
b2, 删除S末尾的元素, 使S与T相等, 则此时edit[m][n] = edit[m - 1][n] + 1;
b3, 删除T末尾的元素, 使T与S相等, 则此时edit[m][n] = edit[m][n - 1] + 1;
b4, 在S的末尾添加T的尾元素, 使S和T相等, 则此时S的长度变为m+1, 但是此时S和T的末尾元素已经相等, 只需要比较S的前m个元素与T的前n-1个元素, 所以满足edit[m][n] = edit[m][n - 1] + 1;
b5, 在T的末尾添加S的尾元素, 使T和S相等, 此时的情况跟b4相同, 满足edit[m][n] = edit[m - 1][n] + 1;
c, 比较特殊的情况是, 当S为空时, edit[0][n] = n; 而当T为空时, edit[m][0] = m; 这个很好理解, 例如对于序列""和"abc", 则两者的最少操作为3, 即序列""进行3次插入操作, 或者序列"abc"进行3次删除操作.
所以, 以上我们不难推出编辑距离的动态规划方程为:

dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+flag)   if a[i] == b[j]: flag = 0 if a[i] != b[j]: flag = 1


可能存在如下情况所有取 min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+flag)：


  A： ******cc  B： *******c    a[i-1] = ******c b[j]: ******c   所以A B末尾相同不一定采取dp[i-1][j-1]


'''


def distance(string1,string2):
    len1 = len(string1)
    len2 = len(string2)


    dp = [[0]*(len2+1) for i in range(len1+1)]

    for i in range(1,len1+1):
        dp[i][0] = i

    for j in range(1,len2+1):
        dp[0][j] = j

    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)  #dp[i-1][j-1]+1 为替换操作
    return dp[len1][len2]



if __name__ == '__main__':
    S = "sailn"
    T = "failing"
    print(distance(S,T))
    pass