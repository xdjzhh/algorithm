'''
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 

和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

输入: [3,1,5,8]
输出: 167

这是一道DP（动态规划）的题目，看到这种求极值的问题，应该首先想到利用动态规划去思考思路。本题为Hard题目，难点在于如何建立DP数组，以及推导出递推公式。

我们首先建立一个二维数组dp[i][j]，用来表示在区间i到j范围内戳破所有气球能得到的最大分数，通过递推公式逐步求解，最终dp[0][length-1]即为题目答案。

接下来，看下如何写出推导公式。对于，任意一个区间[i, j]，如果我们想戳破一个气球k，k在i和j的范围内(i <= k <= j)，这时我们可以将这个区间变为三个部分：

[i, k - 1], [k], [k + 1, j] // k在i和j中间
[i, k - 1], [k], []         // k等于j
[], [k], [k + 1, j]         // k等于i
[], [k], []                 // k == i == j
不论k在i和j中间的什么位置，我们都可以将这一段分为3个子问题，我们分别称这三部分为：左，中，右。中间部分是我们这一步想要戳破的气球，它的长度永远只会是1

（因为我们不能同时戳两个球）。左右两部分则分别是 dp[i][j] 的子问题 dp[i][k-1] 和 dp[k+1][j] 的解。根据题目，中间部分的值 dp[k][k] 则应该是

nums[k] * nums[k’ left] * nums[k’ right]。那么k的左和右是哪两个位置的值呢？显然 k-1 和 k+1 并不是正确答案，原因很简单，不论k-1还是k+1，

他们都存在于左右两个子问题中，我们定义的dp数组是代表该区间内所有气球都已经戳破的条件下，既然已经被戳破，那么我们就不能再利用这个值了，因此，k坐标的

左右相邻的气球坐标应该是当前i和j范围的相邻位置，即i-1和j+1。至此，我们可以清晰的写出推导公式：

dp[i][j] = Max(dp[i][k-1] + nums[k] * nums[i-1] * nums[j+1] + dp[k+1][j]);

'''

def solution(coin):
    length = len(coin)
    coin.insert(0,1)
    coin.append(1)
    dp = [[0]*len(coin) for i in range(len(coin))]
    for l in range(1,length+1):
        for i in range(1,length-l+2):
            j = i + l -1
            for k in range(i,j+1):
                dp[i][j] = max(dp[i][j],dp[i][k-1]+dp[k+1][j]+coin[k]*coin[i-1]*coin[j+1])
    for i in dp:
        print(i)
    return dp[1][length]




if __name__ == '__main__':
    coin = [3,1,5,8]
    print(solution(coin))