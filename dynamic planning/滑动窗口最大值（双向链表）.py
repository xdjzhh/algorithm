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
    if nums == []:
        return []
    if k == 1:
        return nums

    # result = [max(nums[:k])]
    window = []
    '''对最初的window中的k个元素做处理，使其变成从最大值开始到第k个元素的筛选过的降序排列的数组：
        [1,4,1,3,2,1,5,7,2,4] k = 5 ==> innit_window[4,3,2] 最大值为 init_window[0]
    '''
    for init_index in range(0, k):
        while window != [] and nums[window[-1]] < nums[init_index]:
            window.pop(-1)
        window.append(init_index)

    result = [nums[window[0]]]

    for index in range(k, len(nums)):
        if window != [] and index - window[0] == k:
            window.pop(0)

        print(window)
        while window != [] and nums[window[-1]] < nums[index]:
            window.pop(-1)

        window.append(index)
        result.append(nums[window[0]])

    return result

if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(solution(nums,k))