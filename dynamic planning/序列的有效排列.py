'''
903. DI 序列的有效排列
我们给出 S，一个源于 {'D', 'I'} 的长度为 n 的字符串 。（这些字母代表 “减少” 和 “增加”。）
有效排列 是对整数 {0, 1, ..., n} 的一个排列 P[0], P[1], ..., P[n]，使得对所有的 i：

如果 S[i] == 'D'，那么 P[i] > P[i+1]，以及；
如果 S[i] == 'I'，那么 P[i] < P[i+1]。
有多少个有效排列？因为答案可能很大，所以请返回你的答案模 10^9 + 7.



示例：

输入："DID"
输出：5
解释：
(0, 1, 2, 3) 的五个有效排列是：
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)

解答：
假如我们现在已经有了一个 "DID" 模式的序列 1032，假如我们还想加一个D，变成 "DIDD"，该怎么加数字呢？多了一个模式符，就多了一个数字4，
显然直接加4是不行的，实际是可以在末尾加2的，但是要先把原序列中大于等于2的数字都先加1，即 1032 -> 1043，然后再加2，变成 10432，就是
"DIDD" 了。虽然我们改变了序列的数字顺序，但是升降模式还是保持不变的。同理，也是可以加1的，1032 -> 2043 -> 20431，也是可以加0的，
1032 -> 2143 -> 21430。但是无法加3和4，因为 1032 最后一个数字2很很重要，所有小于等于2的数字，都可以加在后面，从而形成降序。那么反过
来也是一样，若要加个升序，比如变成 "DIDI"，猜也猜的出来，后面要加（必须）大于2的数字，然后把所有大于等于这个数字的地方都加1，比如加上3，
1032 -> 1042 -> 10423，再比如加上4，1032 -> 1032 -> 10324。

'''


class Solution:
    def numPermsDISequence(self, S: str) -> int:
        mod = 1000000007
        dp = [[0] * (len(S) + 1) for i in range(len(S) + 1)]

        dp[0][0] = 1

        for i in range(1, len(S) + 1):
            for j in range(i + 1):
                if S[i - 1] == 'D':
                    '''根据j的大小判断 前i-1的序列的最后一位 必须是大于等于j的值'''
                    for k in range(j, i):
                        dp[i][j] = dp[i - 1][k] + dp[i][j] % mod
                else:
                    '''根据j的大小判断 前i-1的序列的最后一位 必须是小于j的值'''
                    for k in range(j):
                        dp[i][j] = dp[i - 1][k] + dp[i][j] % mod

        ans = 0
        for i in range(len(S) + 1):
            ans += dp[len(S)][i]

        return ans % mod