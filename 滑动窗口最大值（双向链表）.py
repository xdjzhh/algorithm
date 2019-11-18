'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

详解链接 https://leetcode-cn.com/problems/sliding-window-maximum/solution/shi-pin-jie-xi-shuang-duan-dui-lie-hua-dong-chuang/
'''

def solution(nums,k):

    result = [max(nums[0:k])]
    temp_index = [nums.index(max(nums[0:k]))]

    for i in range(k,len(nums)):
        if temp_index and (i - temp_index[-1] == i-k):
            temp_index.pop(0)
            '''此循环是为了pop掉tempindex【0】和tempindex【-1】数值之间的数，形成递减列表'''
        while temp_index and (nums[temp_index[-1]] < nums[i]):
            temp_index.pop()
        temp_index.append(i)
        result.append(nums[temp_index[0]])
    return result

if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(solution(nums,k))