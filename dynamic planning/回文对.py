'''
给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

示例 1:

输入: ["abcd","dcba","lls","s","sssll"]
输出: [[0,1],[1,0],[3,2],[2,4]]
解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2:

输入: ["bat","tab","cat"]
输出: [[0,1],[1,0]]
解释: 可拼接成的回文串为 ["battab","tabbat"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words_dict = {}
        for i in range(len(words)):
            words_dict[words[i]] = i
        result = []
        for i in range(len(words)):
            rev_word = words[i][::-1]
            if rev_word in words_dict and words_dict[rev_word] != i:
                result.append([i, words_dict[rev_word]])

            '''下面两个循环的index要剔除上个if的情况，否则会出现重复'''

            for j in range(len(words[i])):
                print(words[i][j + 1:][::-1])
                if words[i][:j + 1] == words[i][:j + 1][::-1] and words[i][j + 1:][::-1] in words_dict:
                    if words_dict[words[i][j + 1:][::-1]] != i:
                        result.append([words_dict[words[i][j + 1:][::-1]], i])

            for j in range(len(words[i])):
                if words[i][j:] == words[i][j:][::-1] and words[i][:j][::-1] in words_dict:
                    if words_dict[words[i][:j][::-1]] != i:
                        result.append([i, words_dict[words[i][:j][::-1]]])

        print(result)

        return result