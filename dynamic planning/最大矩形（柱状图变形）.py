'''

给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
'''

'''构造柱状图（栈）'''


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        dp = [0 for i in range(len(matrix[0]))]
        max_result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[j] += 1
                else:
                    dp[j] = 0
            max_result = max(max_result, self.loops(dp))
        return max_result

    def loops(self, dp):
        stack = [-1]
        max_area = 0
        for index in range(len(dp)):
            while stack[-1] != -1 and dp[stack[-1]] > dp[index]:
                pop_num = stack.pop(-1)
                max_area = max(max_area, dp[pop_num] * (index - stack[-1] - 1))
            stack.append(index)

        while stack[-1] != -1:
            pop_num = stack.pop(-1)
            max_area = max(max_area, dp[pop_num] * (len(dp) - stack[-1] - 1))

        return max_area


'''动态规划'''


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0

        right = [len(matrix[0])] * len(matrix[0])
        left = [0] * len(matrix[0])
        height = [0] * len(matrix[0])

        max_area = 0

        for i in range(len(matrix)):
            current_left = 0
            current_right = len(matrix[0])
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    height[j] = height[j] + 1
                else:
                    height[j] = 0

            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    '''当matrix里元素为0时，重置left【j】，不参与下一行计算，current_left标示当前元素最左边非0元素的位置，若上一行left[j]有值时与当前current_left比较，取最大为左边index'''
                    left[j] = max(left[j], current_left)
                else:
                    left[j] = 0
                    current_left = j + 1

            for j in range(len(matrix[0]) - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], current_right)
                else:
                    right[j] = len(matrix[0])
                    current_right = j

            for j in range(len(matrix[0])):
                max_area = max(max_area, height[j] * (right[j] - left[j]))
        return max_area
