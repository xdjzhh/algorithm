'''76. 最小覆盖子串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。'''
from collections import *


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = Counter(t)
        window_dict = {}
        l, r = 0, 0
        result = (float('inf'), l, r)
        required = len(t_dict)
        current = 0

        while r < len(s):
            character = s[r]
            window_dict[character] = window_dict.get(character, 0) + 1
            if character in t_dict and window_dict[character] == t_dict[character]:
                current += 1

            while l <= r and current == required:
                character = s[l]
                if r - l + 1 < result[0]:
                    result = (r - l + 1, l, r)
                window_dict[character] = window_dict.get(character) - 1
                if character in t_dict and window_dict[character] < t_dict[character]:
                    current -= 1

                l += 1

            r += 1
        if result[0] == float('inf'):
            return ""
        else:
            return s[result[1]:result[2] + 1]
