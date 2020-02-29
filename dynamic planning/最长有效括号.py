'''32. 最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''

'''动态规划'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 1:
            return 0

        dp = [0 for i in range(len(s))]

        max_len = 0

        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    '''防止出现dp[-1]的情况'''
                    if i - 2 >= 0:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                if s[i - 1] == ')':
                    if s[i - dp[i - 1] - 1] == '(' and i - dp[i - 1] - 1 >= 0:
                        '''防止出现dp[-1]的情况'''
                        if i - dp[i - 1] >= 2:
                            dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                        else:
                            dp[i] = dp[i - 1] + 2
                    else:
                        dp[i] = 0
                max_len = max(max_len, dp[i])
        return max_len



'''重点：栈'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 1:
            return 0
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)

            else:
                stack.pop(-1)
                if stack != []:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)

        return max_len
