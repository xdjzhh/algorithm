
'''
栈 一般都会在stack 中增加-1，计算仅有 头与 当前位置时的情况


'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for index in range(len(heights)):
            '''注意 智慧处理到栈中最后一个比 现在大的情况 [6,7,3,2,4,5,9,4,3] index为3 小于 index为7 所以不会执行'''
            while stack[-1] != -1 and heights[stack[-1]] > heights[index]:
                back_index = stack.pop(-1)
                max_area= max(max_area,heights[back_index]*(index-stack[-1]-1))
            stack.append(index)
        while stack[-1] != -1:
            back_index = stack.pop(-1)
            max_area= max(max_area,heights[back_index]*(len(heights)-stack[-1]-1))
        return max_area