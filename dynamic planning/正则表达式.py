'''
10. 正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if (len(p) == 0):
            return not s
        if (len(p) == 1) and (len(s) != 1):
            return False

        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]

        dp[0][0] = True
        dp[0][1] = False
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if (s[i - 1] == p[j - 1]) or (p[j - 1] == '.'):
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if (p[j - 2] == '.') or (p[j - 2] == s[i - 1]):
                        '''判断 要么.*为0   或者 s中有多个 a* 中的a（s：aaaa  p： a*）或者s中只有一个a*'''
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j] or dp[i][j-1]
                    else:
                        dp[i][j] = dp[i][j - 2]
                else:
                    dp[i][j] = False
        return dp[len(s)][len(p)]