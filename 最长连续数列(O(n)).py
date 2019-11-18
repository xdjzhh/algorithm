'''
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

想法

其实我们一开始的暴力解法的思路是正确的，但是需要进行一些优化，才能达到 O(n)O(n) 的时间复杂度。

算法

这个优化算法与暴力算法仅有两处不同：这些数字用一个 HashSet 保存（或者用 Python 里的 Set），实现 O(1)O(1) 时间的查询，同时，

我们只对 当前数字 - 1 不在哈希表里的数字，作为连续序列的第一个数字去找对应的最长序列，这是因为其他数字一定已经出现在了某个序列里。

'''

def solution(num):
    num = set(num)
    longest =0
    for each in num:
        if each-1 not in num:
            start = each
            each_long = 1
            while start+1 in num:
                start+=1
                each_long+=1
        longest = max(longest,each_long)
    return longest

    pass


if __name__ == '__main__':
    num = [100, 4, 200, 1, 3, 2]
    print(solution(num))