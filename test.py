from collections import *
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        result = []
        array_dict = Counter(array)
        for i in array:
            if array[i] == 1:
                result.append(i)
        print(result)

list1 = [2,4,3,6,3,2,5,5]
solution = Solution()
print(solution.FindNumsAppearOnce(list1))